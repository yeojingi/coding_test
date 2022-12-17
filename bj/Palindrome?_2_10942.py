import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
boards = [ list(map(int, input().split())) for _ in range(M) ]

dp = [ [-1] * N for _ in range(N) ]
fg = [ [0] * N for _ in range(N) ]

for i in range(N):
  dp[i][i] = 1
  if i+1 < N:
    dp[i][i+1] = 1

def rec(cs, ce):
  ns = cs + 1
  ne = ce - 1

  if arr[cs] != arr[ce]:
    return 0

  if dp[ns][ne] == 1:
    return 1
  elif dp[ns][ne] == 0:
    return 0
  elif dp[ns][ne] == -1:
    return rec(ns, ne)

for board in boards:
  [S, E] = board

  cs = S - 1
  ce = E - 1

  if dp[cs][ce] == -1:
    dp[cs][ce] = rec(cs, ce)
  print(dp[cs][ce])

# print(*dp, sep="\n")
# for ans in anss:
#   print(ans)