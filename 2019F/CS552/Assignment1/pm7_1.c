#include	<stdio.h>
#include	<sys/shm.h>
#include	<sys/stat.h>

int	global;

int	main(	){
  int	segment_id;
  int	*p;
  int	pid;
  segment_id = shmget(IPC_PRIVATE, sizeof(int), S_IRUSR|S_IWUSR);
  p = (int*)shmat(segment_id,	NULL,0);
  *p = 0;
  global = 0;
  pid = fork();
  if (pid	==	0) {
    global = 1;
    printf("This is process A. global=%d\n",	global);
    *p=1;
    exit(0);
  }
  if (pid	>	0){
    while (*p	== 0);
    printf("This is process	B, global=%d.\n",	global);
  }
  shmdt(p);
}
