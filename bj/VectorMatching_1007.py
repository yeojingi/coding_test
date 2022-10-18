from itertools import combinations
import math
import sys

input = sys.stdin.readline


T = int(input())
anss = []
for _ in range(T):
  N = int(input())
  points = []

  for _ in range(N):
    points.append(list(map(int, input().split())))
  
  minLength = math.inf

  combs = list(combinations([i for i in range(N)], N//2))

  for comb in combs:
    vect = [0, 0]
    for i in range(N):
      if i in comb:
        vect[0] += points[i][0]
        vect[1] += points[i][1]
      else:
        vect[0] -= points[i][0]
        vect[1] -= points[i][1]
    
    length = math.sqrt(vect[0] ** 2 + vect[1] ** 2)

    if minLength > length:
      minLength = length
  
  anss.append(minLength)
      

for ans in anss:
  print("%.6f"%ans)