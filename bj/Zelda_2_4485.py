import math
from queue import PriorityQueue


N = int(input())
anss = []
i = 1
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

while N != 0:
  rows = [list(map(int, input().split(' '))) for _ in range(N)]
  dp = [ [math.inf] * N for _ in range(N)]
  dp[0][0] = rows[0][0]
  q = PriorityQueue()
  q.put((dp[0][0], 0, 0))

  while not q.empty():
    [cv, ci, cj] = q.get()

    for k in range(4):
      ni = ci + di[k]
      nj = cj + dj[k]

      if not (ni >= 0 and ni < N and nj >= 0 and nj < N):
        continue

      newValue = rows[ni][nj] + cv
      originalValue = dp[ni][nj]

      if newValue < originalValue:
        dp[ni][nj] = newValue
        q.put((newValue, ni, nj))

  anss.append(f"Problem {i}: {dp[N-1][N-1]}")

  N = int(input())
  i += 1

for ans in anss:
  print(ans)