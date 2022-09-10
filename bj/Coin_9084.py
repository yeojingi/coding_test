from copy import deepcopy


T = int(input())
ans = []
for _ in range(T):
  N = int(input())
  coins = list(map(int, input().split(' ')))
  goal = int(input())

  dp = [0] * (goal+1)
  # for coin in coins:
  #   if coin <= goal:
  #     dp[coin] = 1

  for coin in coins:
    ndp = deepcopy(dp)
    for d in range(goal+1):
      if d- coin == 0:
        dp[d] += 1
      if d - coin > 0:
        dp[d] = dp[d - coin] + ndp[d]
      # print(dp)
  
  ans.append(dp[goal])

for a in ans:
  print(a)