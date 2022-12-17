#include <iostream>

#define BUFF 1000000

int main()
{
  char str[BUFF];
  char *ch;
  int key;

  int hits[26];

  for (int i = 0; i < 26; i++) {
    hits[i] = 0;
  }

  std::cin >> str;
  ch = str;

  while (*ch != '\0') {
    key = *ch - 65;
    if (*ch >= 91) {
      key -= 32;
    }
    hits[key] ++;

    ch ++;
  }

  int maxIndex, maxValue = -1;

  for (int i = 0; i < 26; i++) {
    if (hits[i] > maxValue) {
      maxValue = hits[i];
      maxIndex = i;
    } else if (hits[i] == maxValue) {
      maxIndex = '?' - 65;
    }
  }

  std::cout << char(maxIndex+65) << "\n";
}