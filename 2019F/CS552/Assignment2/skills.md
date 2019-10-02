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
