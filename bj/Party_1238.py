import math


N, M, X = map(int, input().split(' '))
dp = [ [math.inf] * (N+1) for _ in range(N+1)]

for _ in range(M):
  s, e, t = map(int, input().split(' '))
  dp[s][e] = t

for k in range(1, N+1):
  for i in range(1, N+1):
    for j in range(1, N+1):
      dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

maxValue = 0
maxIndex = 0

for i in range(1, N+1):
  value = dp[i][X] + dp[X][i]
  if maxValue < value:
    maxValue = value
    maxIndex = i

# print(*dp, sep="\n")
print(maxValue)