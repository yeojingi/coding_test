from collections import deque
from copy import deepcopy
from queue import PriorityQueue


N = int(input())
rows = [ list(map(int, input().split(' '))) for _ in range(N) ]
dp = [ [-1] * N for _ in range(N) ]

startPoint = []
for i in range(N):
  for j in range(N):
    if rows[i][j] == 9:
      rows[i][j] = 0
      dp[i][j] = 0

      startPoint = [i, j]
      break
  if startPoint:
    break

t = 0
sizeOfShark = 2
p = 0
ans = t

di = [-1, 0, 0, 1]
dj = [0, -1, 1, 0]

v = deque()
v.append([*startPoint, 0])

tempV = PriorityQueue()

while v:
  [ci, cj, t] = v.popleft()

  if rows[ci][cj] != 0 and rows[ci][cj] < sizeOfShark:
    p += 1
    rows[ci][cj] = 0
    v = deque([[ci, cj, t]])
    tempV = PriorityQueue()
    ans = t

    if p >= (sizeOfShark + 2) * (sizeOfShark - 1) / 2:
      sizeOfShark += 1
    # print(*rows, sep="\n")
    # print(ci, cj, t, sizeOfShark)
    # input()
    continue

  for k in range(4):
    ni = ci + di[k]
    nj = cj + dj[k]

    if not (ni >= 0 and ni < N and nj >= 0 and nj < N):
      continue

    if rows[ni][nj] <= sizeOfShark and dp[ni][nj] < p:
      dp[ni][nj] = p
      tempV.put((ni, [ni, nj, t+1]))
  
  if not v:
    while not tempV.empty():
      v.append(tempV.get()[1])

print(ans)