#include <iostream>

int main ()
{
  int N, cur, ti;
  int arr[1000000];

  std::cin >> N;

  for (int i = 0; i < N; i++)
  {
    std::cin >> arr[i];
  }

  for (int i = 0; i < N; i++)
  {
    cur = arr[i];
    ti = i;
    for (int j = i; j < N; j++)
    {
      if (arr[j] < arr[ti])
      {
        ti = j;
      }
    }
    arr[i] = arr[ti];
    arr[ti] = cur;
  }

  for (int i = 0; i < N; i++)
  {
    std::cout << arr[i] << "\n";
  }
}