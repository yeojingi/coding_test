s1 = input()
N = len(s1)
s2 = input()
M = len(s2)

dp = [ [0] * (N+1) for _ in range(M+1)]
# for j in range(M+1):
#   dp[j][0] = 1

# for i in range(N+1):
#   dp[0][i] = 1

for i in range(1, M+1):
  c2 = s2[i-1]
  for j in range(1, N+1):
    c1 = s1[j-1]

    if c1 == c2:
      dp[i][j] = dp[i-1][j-1] + 1
    else:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# print(*dp, sep="\n")
print(dp[M][N])