#include <iostream>

int main()
{
  int N, score = 0;
  int arr[100];

  int prime[1001];

  std::cin >> N;

  for (int i = 0; i < N; i++)
  {
    std::cin >> arr[i];
  }

  for (int i = 1; i <= 1000; i++)
  {
    prime[i] = 0;
  }

  prime[1] = 1;

  for (int i = 2; i <= 1000; i++)
  {
    for (int j = 2; i * j <= 1000; j++)
    {
      prime[i * j] = 1;
    }
  }

  for (int i = 0; i < N; i ++)
  {
    if (prime[ arr[i] ] == 0)
    {
      score++;
    }
  }

  std::cout<<score<<"\n";

  return 0;
}