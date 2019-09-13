#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
int main()
{
  for(int i=0;i<3;i++)
    if(fork()>0)
      printf("A\n");
}
