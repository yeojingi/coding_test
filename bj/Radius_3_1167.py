# 플로이드 워셜을 시도했으나, 메모리 초과임. 사실 예상했지. 그냥 한번 짜봤음

import math


N = int(input())
edges = [ [] for _ in range(N+1) ]

for _ in range(N):
  stream = list(map(int, input().split(' ')))
  index = stream[0]
  for i in range(1, len(stream)-1, 2):
    edges[index].append([stream[i], stream[i+1]])

formerStartPoint = 0

sp = [ [math.inf] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
  edge = edges[i]
  for e in edge:
    sp[i][e[0]] = e[1]

# print(edges)
# print(*sp, sep="\n")
# print()

for k in range(1, N+1):
  for i in range(1, N+1):
    for j in range(1, N+1):
      # if sp[i][k] + sp[k][j] < sp[i][j]:
      #   print(i, j, k, sp[i][k], sp[k][j], sp[i][j])
      #   print(*sp, sep="\n")
      #   print()
      sp[i][j] = min(sp[i][j], sp[i][k] + sp[k][j])
# print(*sp, sep="\n")

maxValue = 0
for i in range(1, N+1):
  for j in range(1, N+1):
    if i == j:
      continue
    if sp[i][j] > maxValue:
      maxValue = sp[i][j]

print(maxValue)