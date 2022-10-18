#include <stdio.h>
#include <stdlib.h>

int main() {
  int N, M;
  scanf("%d %d", &N, &M);

  char **unseens, **unheards;
  char *name;
  char arr[20];

  unseens = (char*)malloc(sizeof(char*) * N);
  unheards = (char*)malloc(sizeof(char*) * M);

  for (int i = 0; i < N; i++) {
    name = malloc(sizeof(char) * 20);
    scanf("%s", name);
    unseens[i] = name;
  }

  for (int i = 0; i < M; i++) {
    name = malloc(sizeof(char) * 20);
    scanf("%s", name);
    unheards[i] = name;
  }
  
  

  free(unseens);
  free(unheards);

  return 0;
}