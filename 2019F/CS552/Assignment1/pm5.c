#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>

int main( ){
  pid_t pid, pid1;
  pid = fork();
  if (pid < 0) {
    printf(stderr, "Fork Failed");
    exit(1);
  }else if (pid == 0){
    pid1 = getpid();
    printf("chid: pid = %d\n", pid); /* A */
    printf("child: pid = %d\n", pid1); /* B */
  }else{
    pid1 = getpid();
    printf("parent: pid = %d\n", pid); /* C */
    printf("parent: pid = %d\n", pid1); /* D */
    wait(NULL);
  }
  return 0;
}
