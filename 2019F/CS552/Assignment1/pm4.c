#include <unistd.h>
#include <stdio.h>

int main(){
  int i;
  // printf("A\n");
  for(i=0;i<3;i++) {
    if(i%2==1) {
      fork();
    } else {
      fork();
      fork();
    }
  }
}
