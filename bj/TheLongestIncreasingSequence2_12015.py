# import sys

# input = sys.stdin.readline

# N = int(input())
# seq = list(map(int, input().split()))

from random import randrange


N = 10000
seq = [N-i for i in range(N)]
print(seq)
dp = [[seq[0], 1]]
cal = 0

def bisect(dp, v):
  global cal
  
  s = 0
  e = len(dp)
  while s < e:
    cal += 1
    m = (s + e) // 2

    if v < dp[m][0]:
      e = m
    else:
      s = m + 1
  return s - 1

maxValue = 1
for i in range(1, len(seq)):
  dpi = bisect(dp, seq[i])

  nv = dp[dpi][1] + 1
  if nv > maxValue:
    maxValue = nv
  if dp[dpi][0] == seq[i]:
    dp[dpi][1] = nv
  else:
    # print(dp)
    dp.insert(dpi+1, [seq[i], nv])
    # dp = dp[:dpi] + [seq[i], nv] + dp[dpi+1:]
    # print(dp)

print(maxValue, cal, N > cal)