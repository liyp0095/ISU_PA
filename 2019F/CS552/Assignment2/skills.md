# skills from assignment 2

## struct

```c
struct myStruct {
  int a;
  int b;
}

typedef struct MySem {
  sem_t mutex;
  sem_t fmutex;
  sem_t wmutex;
  int nreader;
} Sem;

struct myStruct s1;
s1.a;
struct myStruct *s2;
s2->a;

```

## share memory

```c
#include <sys/stat.h>
#include <sys/shm.h>

int segment_id;
// get a memory space
segment_id = shmget(IPC_PRIVATE, sizeof(Sem), S_IRUSR | S_IWUSR);
// get a pointer to the space to handle it
p_sem = (Sem *) shmat(segment_id, NULL, 0);

// free the handle
shmdt(p_sem);
// delete the memory space
shmctl(segment_id, IPC_RMID, NULL); //remove the shared memory

```

## semaphore

```c
/* sem_open(), sem_destroy(), sem_wait().. */
#include <semaphore.h>      
// user mode

// init pointer of semaphore, could use by other process, value
sem_init(&p_sem->mutex, 1, 1);

// usage
sem_post(&s->mutex);
// control section.
sem_post(&s->mutex);

// destroy, cause error
sem_destory(&p_sem->mutex);
```

## others
```c
#include <unistd.h> /* sleep */
#include <sys/types.h>
#include <sys/wait.h> /*wait*/
```
