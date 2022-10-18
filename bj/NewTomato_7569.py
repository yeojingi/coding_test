from collections import deque


M, N, H = map(int, input().split(' '))

stacks = [ [ list(map(int, input().split(' '))) for _ in range(N)] for _ in range(H)]

di = [1, -1, 0, 0, 0, 0]
dj = [0, 0, 1, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

numUnrotten = M*N*H
dp = [ [ [-1] * M for _ in range(N)] for _ in range(H)]
q = deque()
for h in range(H):
  for i in range(N):
    for j in range(M):
      cur = stacks[h][i][j]

      if cur == 1:
        numUnrotten -= 1
        dp[h][i][j] = 0
        q.append([h, i, j])
      elif cur == -1:
        numUnrotten -= 1
        dp[h][i][j] = 0

maxDay = 0
while q:
  [ch, ci, cj] = q.popleft()

  curDay = dp[ch][ci][cj]

  # if maxDay < curDay:
  #   maxDay = curDay
  
  for k in range(6):
    nh = ch + dh[k]
    ni = ci + di[k]
    nj = cj + dj[k]

    if not (nh >= 0 and nh < H and ni >= 0 and ni < N and nj >= 0 and nj < M):
      continue

    if dp[nh][ni][nj] != -1:
      continue

    dp[nh][ni][nj] = curDay + 1
    maxDay = curDay + 1
    numUnrotten -= 1
    q.append([nh, ni, nj])

if numUnrotten > 0:
  print(-1)
else:
  print(maxDay)