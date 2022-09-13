n, k = map(int, input().split(' '))
coins = [int(input()) for _ in range(n)]
dp = [0] * (k+1)
dp[0] = 1

coins.sort()
for c in range(n):
  for i in range(1, k+1):
    be = i - coins[c]
    if be >= 0:
      dp[i] += dp[be]

# print(dp)
print(dp[k])