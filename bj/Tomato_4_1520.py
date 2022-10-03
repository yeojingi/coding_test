from collections import deque


M, N = map(int, input().split(' '))
rows = [ list(map(int, input().split(' '))) for _ in range(N) ]

q = deque()

for i in range(N):
  for j in range(M):
    if rows[i][j] == 1:
      q.append([i, j])

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

while q:
  [ci, cj] = q.popleft()
  cv = rows[ci][cj]
  # print(ci, cj, cv)
  # print(*rows, sep="\n")
  
  for k in range(4):
    ni = ci + di[k]
    nj = cj + dj[k]

    if not (ni >= 0 and ni < N and nj >= 0 and nj < M):
      continue

    if (rows[ni][nj] != -1 and rows[ni][nj] > cv+1):
      q.append([ni, nj])
      rows[ni][nj] = cv+1
    elif (rows[ni][nj] == 0):
      q.append([ni, nj])
      rows[ni][nj] = cv+1

noZero = True
maxDay = 0

for i in range(N):
  for j in range(M):
    if rows[i][j] == 0:
      noZero = False
    if maxDay < rows[i][j]:
      maxDay = rows[i][j]

if noZero:
  print(maxDay -1)
else:
  print(-1)