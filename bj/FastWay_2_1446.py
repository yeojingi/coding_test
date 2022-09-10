import math

N, D = map(int, input().split(' '))
ways = [list(map(int, input().split(' '))) for _ in range(N)]
ways.sort(key=lambda x: x[1])

sw = 0
dp = [math.inf] * (D+1)
dp[0] = 0

for i in range(1, D+1):
  while sw < N and ways[sw][1] == i:
    dp[i] = min(dp[i], dp[ways[sw][0]] + ways[sw][2])
    sw += 1
  
  dp[i] = min(dp[i], dp[i-1] + 1)

print(dp[D])