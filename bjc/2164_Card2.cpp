#include <iostream>
#include <deque>

int main ()
{
  std::deque<int> q;
  int N, tmp, cnt;

  std::cin >> N;

  for (int i = 1; i <= N; i++)
  {
    q.push_back(i);
  }

  cnt = N;

  while (cnt > 1)
  {
    q.pop_front();
    tmp = q.front();
    q.pop_front();
    q.push_back(tmp);
    cnt--;
  }

  tmp = q.front();
  std::cout << tmp << '\n';
}