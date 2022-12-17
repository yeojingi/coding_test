import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
boards = [ list(map(int, input().split())) for _ in range(M) ]

dp = [ [0] * N for _ in range(N) ]

# for i in range(N):
#   dp[i][i] = 1
#   if i+1 < N:
#     dp[i][i+1] = 1

# for s in range(N-1, -1, -1):
#   for e in range(s+2, N):
for d in range(N):
  for s in range(N-d):
    e = s + d
    if s == e:
      dp[s][e] = 1
      continue
    if s + 1 == e:
      if arr[s] == arr[e]:
        dp[s][e] = 1
      continue
    # print(s, e)
    if arr[s] == arr[e] and dp[s+1][e-1] == 1:
      dp[s][e] = 1

anss = []
for board in boards:
  [S, E] = board

  cs = S - 1
  ce = E - 1
  anss.append(str(dp[cs][ce]))

print("\n".join(anss))
# print(*dp, sep="\n")
# for ans in anss:
#   print(ans)