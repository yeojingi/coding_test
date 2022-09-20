from collections import deque
import math


# M, N = map(int, input().split(' '))
# rows = [ list(map(int, input().split(' '))) for _ in range(N) ]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

M = 1000
N = 1000
rows = [ [0] * M for _ in range(N)]
for i in range(1, N-1, 2):
  for j in range(1, M-1, 2):
    # if ((j+1) // 2) % 2 == 0 and i == 0:
    #   continue
    # elif ((j+1) // 2) % 2 == 1 and i == N-1:
    #   continue
    rows[i][j] = 1
# rows[0][0] = 1
print('?')

dp = [ [math.inf] * M for _ in range(N)]

q = deque()
numGrounds = - M * N
maxDay = 0

cal = 0
for i in range(N):
  for j in range(M):
    if rows[i][j] == 1:
      q.append([i, j, 0])
      dp[i][j] = 0
      numGrounds += 1

    if rows[i][j] == -1:
      numGrounds += 1
      dp[i][j] = 0
    
while q:
  cal += 1
  [ci, cj, d] = q.popleft()
  # print(ci, cj, d)
  
  if d > maxDay:
    maxDay = d

  dp[ci][cj] = d
  
  for k in range(4):
    ni = ci + di[k]
    nj = cj + dj[k]

    if not (ni >= 0 and ni < N and nj >= 0 and nj < M):
      continue

    if rows[ni][nj] == 0 and dp[ni][nj] > d+1:
      q.append([ni, nj, d+1])
      if dp[ni][nj] == math.inf:
        numGrounds += 1
      dp[ni][nj] = d+1

print(*dp, sep="\n")
print(maxDay, numGrounds, cal)
if numGrounds < 0:
  print(-1)
else:
  print(max([ max(row) for row in dp]))