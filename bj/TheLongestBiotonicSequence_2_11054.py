N = int(input())
arr = list(map(int, input().split(' ')))

udp = [0] * N
ddp = [0] * N

def gen_dp(arr, N):
  dp = [1] * N
  for i in range(N):
    maxLength = 1
    cur = arr[i]
    for j in range(i):
      if arr[j] < cur and dp[j] + 1 > maxLength:
        maxLength = dp[j] + 1
    dp[i] = maxLength
  
  return dp

udp = gen_dp(arr, N)
arr.reverse()
ddp = gen_dp(arr, N)
ddp.reverse()

dp = [0]*N
for i in range(N):
  dp[i] = udp[i] + ddp[i]

print(max(dp)-1)
