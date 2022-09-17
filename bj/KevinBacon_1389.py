import math


N, M = map(int, input().split(' '))
paths = [[] for _ in range(N+1)]

dp = [ [math.inf] * (N+1) for _ in range(N+1)]

for _ in range(M):
  s, e = map(int, input().split(' '))
  dp[s][e] = 1
  dp[e][s] = 1

for k in range(1, N+1):
  for i in range(1, N+1):
    for j in range(1, N+1):
      dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

# cands = [ [math.inf] for _ in range(N+1)]
minValue = math.inf
res = 0
for i in range(1, N+1):
  ans = 0
  for k in range(1, N+1):
    if k != i:
      ans += dp[i][k]
  if ans < minValue:
    res = i
    minValue = ans

# print(*dp, sep="\n")
print(res)