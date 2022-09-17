T = int(input())
anss = []
for _ in range(T):
  N = int(input())
  coins = list(map(int, input().split(' ')))
  coins.sort()
  G = int(input())

  dp = [ [0] * (G+1) for _ in range(N)]

  for i in range(N):
    dp[i][0] = 1
    coin = coins[i]
    # print(coin)
    for j in range(1, G+1):
      res = 0
      if i > 0:
        res += dp[i-1][j]
      if j - coin >= 0:
        res += dp[i][j-coin]
      dp[i][j] = res
  
  anss.append(dp[N-1][G])

print(*anss, sep="\n")