N = int(input())
seq = list(map(int, input().split()))

dp = []

def rec(n):
  s = 0
  e = len(dp)

  while s < e:
    m = (s + e) // 2

    c = dp[m]
    if c < n:
      s = m + 1
    else:
      e = m
  
  return s

maxValue = 0
for n in seq:
  i = rec(n)

  if i < len(dp):
    dp[i] = n
  else:
    dp.append(n)
  
  if maxValue < i + 1:
    maxValue = i + 1

print(maxValue)