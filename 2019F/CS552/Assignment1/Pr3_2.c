#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int gVar=0;

int main()
{
  int lVar=0;
  int *p;
  p=(int *)malloc(sizeof(int));
  int pid=fork();
  if(pid>0){
    gVar=1;
    lVar=1;
    *p=1;
    printf("%d, %d, %d\n", gVar, lVar, *p);
  }else{
    gVar=2;
    lVar=2;
    *p=2;
    printf("%d, %d, %d\n", gVar, lVar, *p);
  }
}
