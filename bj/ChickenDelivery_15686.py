from itertools import combinations
import math


N, M = map(int, input().split(' '))
rows = [ list(map(int, input().split(' '))) for _ in range(N)]

chickens = []
homes = []
for i in range(N):
  for j in range(N):
    if rows[i][j] == 1:
      homes.append([i, j])
    elif rows[i][j] == 2:
      chickens.append([i, j])

combs = combinations( [ i for i in range(len(chickens)) ], M)

I = len(homes)
J = len(chickens)

dMatrix = [ [ abs(chickens[j][0] - homes[i][0]) + abs(chickens[j][1] - homes[i][1]) for j in range(J)] for i in range(I) ]

minD = math.inf
for comb in combs:
  candidate = 0
  for i in range(I):
    minI = math.inf
    for c in comb:
      minI = min(dMatrix[i][c], minI)
    candidate += minI
  
  minD = min(candidate, minD)

print(minD)