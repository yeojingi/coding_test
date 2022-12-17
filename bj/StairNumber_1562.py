N = int(input())
n = 1
dp = {i: [0] * 1024 for i in range(10)}
for i in range(10):
  dp[i][2**i] = 1

while n < N:
  ndp = {i: [0] * 1024 for i in range(10)}

  for i in range(10):
    l = i - 1
    h = i + 1

    if 0 <= l:
      for j in range(1024):
        key = j | 2**i
        ndp[i][key] += dp[l][j]
    if h < 10:
      for j in range(1024):
        key = j | 2**i
        ndp[i][key] += dp[h][j]

  dp = ndp
  n += 1

sum = 0
for key, value in dp.items():
  if key == 0:
    continue
  sum += value[1023]
  sum %= 1000000000
print(sum)