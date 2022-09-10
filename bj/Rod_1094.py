N = int(input())

x = N
ans = 0 
while x > 0:
  ans += x % 2
  x = x // 2
print(ans)