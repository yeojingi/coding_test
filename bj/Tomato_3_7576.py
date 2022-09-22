from collections import deque


M, N = map(int, input().split(' '))
rows = [ list(map(int, input().split(' '))) for _ in range(N) ]

v = deque()
unTomato = - N * M
for i in range(N):
  for j in range(M):
    if rows[i][j] == 1:
      v.append([i, j])
    elif rows[i][j] == -1:
      unTomato += 1


di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

cycle = 1
dp = [ [0] * M for _ in range(N)]

while v:
  [ci, cj] = v.popleft()

  if dp[ci][cj] == 0:
    unTomato += 1

  curDay = rows[ci][cj]
  dp[ci][cj] = cycle
  # print(*rows, sep="\n")
  # print(*dp, sep="\n")
  # print(unTomato)
  # input()
  
  for k in range(4):
    ni = ci + di[k]
    nj = cj + dj[k]

    if not (ni >= 0 and ni < N and nj >= 0 and nj < M):
      continue

    if dp[ni][nj] < cycle and rows[ni][nj] != -1 and rows[ni][nj] != 1 and (rows[ni][nj] == 0 or rows[ni][nj] > curDay+1):
      rows[ni][nj] = curDay + 1
      v.append([ni, nj])

if unTomato < 0:
  print(-1)
else:
  print(max( max(row) for row in rows )-1)