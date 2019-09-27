#include	<stdio.h>
#include	<sys/shm.h>
#include	<sys/stat.h>

int main(int argc, char *argv[]) {
  for (auto c: argv[1]) {
    printf("%s", c);
  }
  int	segment_id;
  int	*p;
  int	pid;
  segment_id = shmget(IPC_PRIVATE, sizeof(int), S_IRUSR|S_IWUSR);
  p = (int*)shmat(segment_id,	NULL,0);
  *p = 0;
  printf("%s", argv[1]);
  return 0;
}
