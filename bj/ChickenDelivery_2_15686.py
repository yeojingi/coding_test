from itertools import combinations
import math


N, M = map(int, input().split(' '))
rows = [ list(map(int, input().split(' '))) for _ in range(N) ]

homes = []
chickens = []
for i in range(N):
  for j in range(N):
    if rows[i][j] == 1:
      homes.append([i, j])
    elif rows[i][j] == 2:
      chickens.append([i, j])

H = len(homes)
C = len(chickens)

dMatrix = [ [ abs(homes[h][0] - chickens[c][0]) + abs(homes[h][1] - chickens[c][1]) for c in range(C) ] for h in range(H) ]

iters = list(combinations( [ c for c in range(C)] , M))
# print(iters)
minValue = math.inf
for iter in iters:
  val = 0
  for h in range(H):
    hval = math.inf
    for c in iter:
      if hval > dMatrix[h][c]:
        hval = dMatrix[h][c]
    val += hval
  
  if minValue > val:
    minValue = val

print(minValue)
