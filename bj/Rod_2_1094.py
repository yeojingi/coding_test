a = int(input())

ans = 0
while a > 0:
  ans += a % 2
  a //= 2
print(ans)