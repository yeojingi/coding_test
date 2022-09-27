import math


N = int(input())
arr = list(map(int, input().split(' ')))

dp = [0] * N

lowest = math.inf

for i in range(N):
  cur = arr[i]
  if cur < lowest:
    lowest = cur
  
  dp[i] = cur - lowest

# print(dp)
print(max(dp))