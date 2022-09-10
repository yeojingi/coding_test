import math


N, D = map(int, input().split(' '))
ways = []
for _ in range(N):
  ways.append(list(map(int, input().split(' '))))

ways.sort(key=lambda x: x[0])

dp = [math.inf] * (D+1)
wi = 0
dp[0] = 0

for d in range(D):
  while wi < N and ways[wi][0] == d:
    # print(ways[wi][1])
    if ways[wi][1] <= D:
      dp[ways[wi][1]] = min(dp[d] + ways[wi][2], dp[ways[wi][1]])
    wi += 1
  dp[d+1] = min(dp[d+1], dp[d] + 1)
  
print(dp[D])