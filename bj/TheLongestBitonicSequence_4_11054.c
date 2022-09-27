#include <stdio.h>
#include <stdlib.h>

int main()
{
  int *dp, *udp, *ddp;
  int N, *arr;
  int cur, value;

  scanf("%d", &N);

  arr = malloc(sizeof(int) * N);
  dp = malloc(sizeof(int) * N);
  udp = malloc(sizeof(int) * N);
  ddp = malloc(sizeof(int) * N);

  for (int i = 0; i < N; i++) {
    scanf("%d", arr+i);
    udp[i] = 1;
    ddp[i] = 1;
  }

  for (int i = 0; i < N; i++) {
    value = 1;

    for (int index = 0; index < i; index++) {
      if (arr[index] < arr[i] && udp[index] + 1 > value) {
        value = udp[index] + 1;
      }
    }

    udp[i] = value;
  }

  for (int i = N-1; i >= 0; i--) {
    value = 1;

    for (int index = N-1; index > i; index--) {
      if (arr[index] < arr[i] && ddp[index] + 1 > value) {
        value = ddp[index] + 1;
      }
    }

    ddp[i] = value;
  }

  int max = 0;
  for (int i = 0; i < N; i++) {
    dp[i] = udp[i] + ddp[i];
    if (dp[i] > max) {
      max = dp[i];
    }
  }

  printf("%d\n", max-1);

  return 0;
}