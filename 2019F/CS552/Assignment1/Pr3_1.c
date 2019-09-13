#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
int main()
{
  for(int i=0;i<3;i++) {
    printf("i=%d\n", i);
    if(fork()>0) {
      printf("A\n");
    }
  }
}
