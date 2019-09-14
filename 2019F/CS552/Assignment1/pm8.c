#include <pthread.h>
#include <stdio.h>

int	i;

void *th_code(void	*x)
{
  pthread_t	tid;
  i	=	i	- 1;
  if(i>0) {
    pthread_create(&tid,	NULL,	th_code,	NULL);
    pthread_join(tid,	NULL);
  }
  printf("A\n");
}

int	main()
{
  pthread_t	tid;
  i=3;
  pthread_create(&tid,	NULL,	th_code,	NULL);
  pthread_join(tid,	NULL);
}
