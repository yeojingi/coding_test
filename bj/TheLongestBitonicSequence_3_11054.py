N = int(input())
seq = list(map(int, input().split(' ')))


def gen():
  dp = [1] * N
  for i in range(1, N):
    for j in range(i):
      if seq[j] < seq[i] and dp[j] + 1 > dp[i]:
        dp[i] = dp[j] + 1
  
  return dp

udp = gen()
seq.reverse()
ddp = gen()
ddp.reverse()

sdp = [0] * N
for i in range(N):
  sdp[i] = udp[i] + ddp[i]

print(max(sdp) -1 )