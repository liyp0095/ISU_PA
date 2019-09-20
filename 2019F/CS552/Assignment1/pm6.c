#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int value = 1;

int main(){
  pid_t pid;
  pid = fork();
  if (pid == 0){
    value += 2;
    return 0;
  }else if (pid > 0){
    wait(NULL) ;
    printf("value = %d", value);
    return 0;
  }
}
