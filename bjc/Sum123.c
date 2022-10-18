#include <stdio.h>
#include <stdlib.h>

int main()
{
  int N, n, i;
  int* inputs, *inputPtr;

  scanf("%d", &N);
  inputs = (int*)malloc(sizeof(int) * N);
  inputPtr = inputs;

  for (i = 0; i < N; i ++) {
    scanf("%d", inputPtr++);
  }

  int mi, mv;
  mi = 0;
  mv = 0;

  for (i = 0; i < N; i ++) {
    if (*(inputs + i) > mv) {
      mi = i;
      mv = *(inputs + i);
    }
  }
  
  int* dp;

  dp = (int*)malloc(sizeof(int) * (mv+1));
  dp[0] = 1;

  for (i = 1; i < (mv+1); i++) {
    dp[i] = 0;
    if (i-1 >= 0) {
      dp[i] += dp[i-1];
    }
    if (i-2 >= 0) {
      dp[i] += dp[i-2];
    }
    if (i-3 >= 0) {
      dp[i] += dp[i-3];
    }
  }

  for (i = 0; i < N; i ++) {

    // printf("%d\n", inputs[i]);
    // printf("%d\n", dp[0]);
    printf("%d\n", dp[ inputs[i] ]  );
  }

  return 0;
}