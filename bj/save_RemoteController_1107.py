import math

# input
goal = int(input())
input()
excs = list(map(int, input().split(' ')))

a = list(map(int, "0123456789"))

for exc in excs:
  a.remove(exc)

digit = len(str(goal)) - 1
base = len(a)

def decTo(B, i):
  global a
  if i < B:
    return a[i]

  return decTo(B, int(i / B)) * 10 + a[i % B]

# brute
ans = math.inf
for i in range(0, base ** (digit+1)):
  t = decTo(base, i)
  now = digit+1 + abs(t - goal)
  if ans > now:
    ans = now

# 100
candidate100 = abs(goal - 100)

print(min(ans, candidate100))

# 그냥 틀렸대