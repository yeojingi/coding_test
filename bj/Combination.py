N, M = map(int, input().split(' '))

ans = 1
for i in range(N, N-M, -1):
  ans *= i
denom = 1
for i in range(1, M+1):
  denom *= i

print(int(ans/denom))