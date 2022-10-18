#include <stdio.h>
#include <stdlib.h>

int main()
{
  int a, b, c;
  int *p, *q, *r;

  p = &a;
  scanf("%d", p);
  printf("%d\n", *p);
  
  return 0;
}