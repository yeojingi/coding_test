#include <iostream>

int main ()
{
  char str[1000000], *c, res;
  int alphabets[26], cnt;

  std::cin >> str;

  for (int i = 0; i < 26; i++)
  {
    alphabets[i] = 0;
  }

  c = str;

  while (*c != '\0')
  {
    if (*c > 90)
    {
      alphabets[*c - 97] ++;
    }
    else
    {
      alphabets[*c - 65] ++;
    }
    c++;
  }

  cnt = 0;
  for (int i = 0; i < 26; i ++)
  {
    if (alphabets[i] > cnt)
    {
      cnt = alphabets[i];
      res = i+65;
    }
    else if (alphabets[i] == cnt && alphabets[i] > 0)
    {
      res = '?';
    }
  }

  std::cout << res << "\n";
}