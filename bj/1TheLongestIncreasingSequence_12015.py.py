N = int(input())
seq = list(map(int, input().split(' ')))

dp = [1] * N
dp[N-1] = 1
for i in range(N-1, -1, -1):
  for j in range(i+1, N):
    if seq[i] < seq[j]:
      dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))