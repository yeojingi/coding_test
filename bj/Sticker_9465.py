import sys

input = sys.stdin.readline

T = int(input())

anss = []
for _ in range(T):
  N = int(input())

  rows = []
  rows.append(list(map(int, input().split(' '))))
  rows.append(list(map(int, input().split(' '))))

  dp = [ [0, 0] for _ in range(N)]

  dp[0][0] = rows[0][0]
  dp[0][1] = rows[1][0]

  if N > 1:
    dp[1][0] = dp[0][1] + rows[0][1]
    dp[1][1] = dp[0][0] + rows[1][1]

  for i in range(2, N):
    dp[i][0] = max(dp[i-2][1] + rows[0][i], dp[i-1][1] + rows[0][i])
    dp[i][1] = max(dp[i-2][0] + rows[1][i], dp[i-1][0] + rows[1][i])
  
  anss.append(str(max(dp[N-1][0], dp[N-1][1])))

print(*anss, sep="\n")