N = int(input())
row = list(map(int, input().split(' ')))
dp = [0] * N

for i in range(N):
  cur = row[i]
  maxLength = 1
  for j in range(i):
    if row[j] < cur and dp[j] >= maxLength:
      maxLength = dp[j]+1
  dp[i] = maxLength

print(max(dp))