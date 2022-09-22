N = int(input())
row = list(map(int, input().split(' ')))
dp = [0] * N

for i in range(N):
  if i == 0:
    dp[i] = row[i]
  else:
    dp[i] = max(row[i], dp[i-1] + row[i])
  
print(max(dp))