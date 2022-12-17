from itertools import combinations
import math


T = int(input())

def rec(s, i, N):
  if i == N-1:
    return [s+"+", s+"-"]

  a = rec(s+"+", i+1, N)
  a += rec(s+"-", i+1, N)

  return a

anss = []
for _ in range(T):
  minLength = math.inf
  N = int(input())

  coords = [list(map(int, input().split())) for _ in range(N)]
  
  a = list(combinations([i for i in range(N)], N // 2))
  
  for arr in a:
    x = 0
    y = 0
    arr = set(arr)
    # print(arr)
    for i in range(N):
      if i in arr:
        x += coords[i][0]
        y += coords[i][1]
      else :
        x -= coords[i][0]
        y -= coords[i][1]
  
    length = x**2 + y**2
    if length < minLength:
      minLength = length

  anss.append(minLength)

for ans in anss:
  print(math.sqrt(ans))