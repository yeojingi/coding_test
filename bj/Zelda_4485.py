import math
from queue import PriorityQueue

ans = []
t = 1
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

while True:
  N = int(input())

  visited = []
  if N == 0:
    break
  rows = []
  for _ in range(N):
    rows.append(list(map(int, input().split(' '))))

  dp = [ [math.inf] * N for _ in range(N) ]

  visited = PriorityQueue()
  dp[0][0] = rows[0][0]
  visited.put((dp[0][0], [0, 0]))

  while not visited.empty():
    [ci, cj] = visited.get()[1]
    # print(ci, cj, visited.empty())

    for k in range(4):
      ni = ci + di[k]
      nj = cj + dj[k]

      if not (ni >= 0 and ni < N and nj >= 0 and nj < N):
        continue

      if dp[ni][nj] > dp[ci][cj] + rows[ni][nj]:
        dp[ni][nj] = dp[ci][cj] + rows[ni][nj]
        visited.put((dp[ni][nj], [ni, nj]))

  ans.append(f"Problem {t}: {dp[N-1][N-1]}")
  t += 1

for a in ans:
  print(a)