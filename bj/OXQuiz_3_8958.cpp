#include <iostream>
#include <cstdlib>

int main()
{
  int T, *ans;
  std::cin >> T;
  char str[81];

  ans = (int*)malloc(sizeof(int) * T);

  for (int t = 0; t < T; t++) {
    std::cin >> str;
    
    int i = 0, val = 0, os = 0;
    bool isO = false;

    while (str[i] != '\0') {
      if (str[i] == 'O') {
        os++;
        val += os;
      } else if (str[i] == 'X') {
        os = 0;
      }
      i++;
    }

    *(int*)(ans+t) = val;
  }

  for (int t = 0; t < T; t++) {
    printf("%d\n", *(ans+t));
  }
  return 0;
}