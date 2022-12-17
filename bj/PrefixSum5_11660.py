import sys

input = sys.stdin.readline

N, M = map(int, input().split())

matrix = [ list(map(int, input().split())) for _ in range(N) ]
points = [ list(map(int, input().split())) for _ in range(M) ]

dp = [ [0] * (N+1) for _ in range(N+1) ]

for j in range(N):
  dp[1][j+1] = dp[1][j] + matrix[0][j]

for i in range(1, N):
  for j in range(N):
    dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j] + matrix[i][j]

for point in points:
  [li, lj, ri, rj] = point

  sum = dp[ri][rj]  

  # up
  sum -= dp[li-1][rj]

  # left
  sum -= dp[ri][lj-1]

  # left up
  sum += dp[li-1][lj-1]

  print(sum)