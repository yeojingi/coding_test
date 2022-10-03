from collections import deque
from queue import PriorityQueue


N = int(input())
rows = [ list(map(int, input().split(' '))) for _ in range(N) ]

startPoint = []
for i in range(N):
  for j in range(N):
    if rows[i][j] == 9:
      startPoint = [i, j]
      rows[i][j] = 0
      break
  if startPoint:
    break

ans = 0
t = 0
size = 2
eaten = 0
dp = [ [0] * N for _ in range(N) ]
dp[ startPoint[0] ][ startPoint[1] ] = 1
q = deque()
q.append([*startPoint, 0])
pq = PriorityQueue()

di = [-1, 0, 0, 1]
dj = [0, -1, 1, 0]

while q:
  [ci, cj, ct] = q.popleft()
  track = dp[ci][cj]

  if rows[ci][cj] != 0 and rows[ci][cj] < size:
    t = ct
    eaten += 1
    track += 1
    rows[ci][cj] = 0
    q = deque()
    pq = PriorityQueue()
  
  if eaten >= size:
    size += 1
    eaten = 0
  
  for k in range(4):
    ni = ci + di[k]
    nj = cj + dj[k]

    if not (ni >= 0 and ni < N and nj >= 0 and nj < N):
      continue

    if dp[ni][nj] < track and rows[ni][nj] <= size:
      pq.put((ni, [ni, nj, ct+1]))
      dp[ni][nj] = track
  
  if not q:
    while not pq.empty():
      q.append(pq.get()[1])

print(t)