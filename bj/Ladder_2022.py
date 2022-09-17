import math


m, n, c = map(float, input().split(' '))

high = min(m, n)
low = 0
ans = 0 
while low+0.001 <= high:
  w = (low+high) / 2

  h1 = math.sqrt(m*m - w*w)
  h2 = math.sqrt(n*n - w*w)
  guess_c = (h1*h2) / ( h1 + h2 )
  if guess_c > c:
    low = w
  else:
    high = w

print(low)