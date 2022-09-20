N = int(input())
row = list(map(int, input().split(' ')))

udp = [0] * N
ddp = [0] * N
dp = [0] * N

for i in range(N):
  maxLength = 0

  cur = row[i]
  for j in range(i):
    if row[j] < cur and udp[j] > maxLength:
      maxLength = udp[j]
  udp[i] = maxLength + 1

for i in range(N):
  maxLength = 0

  cur = row[N-1-i]
  for j in range(i):
    k = N - 1 - j
    if row[k] < cur and ddp[k] > maxLength:
      maxLength = ddp[k]
  ddp[N-1-i] = maxLength + 1

for i in range(N):
  dp[i] = udp[i] + ddp[i]

print(max(dp) - 1)