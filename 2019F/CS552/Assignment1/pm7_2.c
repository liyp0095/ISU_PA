#define _GNU_SOURCE
#include <sched.h>
#include <stdlib.h>
#include <stdio.h>

int th_code(void *arg) {
  int i;
  for(i=0;i<2;i++){ void *p;
    p=(void *)malloc(16384);
    p+=16383;
    clone(th_code,p,CLONE_FS,0);
  }
  printf("A\n");
}

int main() {
  th_code(0);
}
