N, M = map(int, input().split(' '))
rows = [list(map(int, input().split(' '))) for _ in range(N)]
dp = [ [-1] * M for _ in range(N) ]
dp[0][0] = 0
dp[N-1][M-1] = 1

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def rec(ci, cj):
  global rows, dp
  
  for k in range(4):
    ni = ci + di[k]
    nj = cj + dj[k]

    if not (ni >= 0 and ni < N and nj >= 0 and nj < M):
      continue

    if rows[ci][cj] <= rows[ni][nj]:
      continue

    # if dp[ni][nj] > 0:
    #   dp[ci][cj] += dp[ni][nj]
    if dp[ni][nj] == -1:
      dp[ni][nj] = 0
      rec(ni, nj)
    
    dp[ci][cj] += dp[ni][nj]
    # print(*dp, sep="\n")
    # print(ci, cj, ni, nj)
  
  # if dp[ci][cj] == 0:
  #   return 0

rec(0, 0)
print(dp[0][0])