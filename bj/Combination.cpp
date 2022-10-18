#include <iostream>

int main()
{
  int n, m;
  std::cin >> n >> m;
  unsigned long long ans = 1;
  for (int i = 0; i < m; i++) {
    ans *= n - i;
    if (ans == 0) {
      std::cout << i << std::endl;
    }
  }

  unsigned long long denominator = 1;
  for (int i = 1; i <= m; i++) {
    denominator *= i;
  }

  std::cout << ans << std::endl;
  return 0;
}