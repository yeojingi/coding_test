from bisect import bisect_left


N = int(input())
seq = list(map(int, input().split()))

dp = [seq[0]]
# maxV = 0

for i in range(N):
  j = bisect_left(dp, seq[i])
  
  # v = j
  if j >= len(dp):
    dp.append(seq[i])
  else:
    dp[j] = seq[i]
  
  # if maxV < v:
  #   maxV = v

# print(bisect_left(dp, seq[-1]), dp)
print(len(dp))