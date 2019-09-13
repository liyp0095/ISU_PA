#include <unistd.h>
#include <stdio.h>

int main()
{
  int fd0[2],fd1[2];
  pipe(fd0);
  pipe(fd1);
  int pid=fork();
  if(pid>0){
    char buf[255];
    read(fd0[0],buf,255);
    printf("A\n");
  }else{
    int pid=fork();
    if(pid>0){
      char buf[255];
      read(fd1[0],buf,255);
      printf("B\n");
      write(fd0[1],"hello!",sizeof("hello!"));
    }else{
      printf("C\n");
      write(fd1[1],"greeting!",sizeof("greeting!"));
      write(fd0[1],"hello again!",sizeof("hello again!"));
    }
  }
}
