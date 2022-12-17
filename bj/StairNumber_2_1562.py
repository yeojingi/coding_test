N = int(input())
dp = [ [0] * 1024 for _ in range(10)]

for i in range(10):
  dp[i][2**i] = 1

for i in range(2, N+1):
  dp_n = [ [0] * 1024 for _ in range(10) ]
  for j in range(10):
    for k in range(1024):

      if j - 1 >= 0:
        dp_n[j][ k | 2**j ] += dp[j-1][k]
      if j + 1 <= 9:
        dp_n[j][ k | 2**j ] += dp[j+1][k]
  
  dp = dp_n

res = 0
for i in range(1, 10):
  res += dp[i][1023] % 1000000000
  
  # for j in range(1024):
  #   if dp[i][j] == 1:
  #     print(i, "{0:b}".format(j), dp[i][j], end=" | ")
  # print()
print(res)