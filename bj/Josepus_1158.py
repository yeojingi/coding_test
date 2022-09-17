N, K = map(int, input().split(' '))

ans = "<"

l = 0
i = 0
dp = [i+1 for i in range(N)]
while dp:
  i = (i+K-1) % len(dp)

  if l == N-1:
    ans += f"{dp[i]}>"
    break
  else:
    ans += f"{dp[i]}, "
    dp = dp[:i] + dp[i+1:]
    # print(i, dp)
  l += 1

print(ans)