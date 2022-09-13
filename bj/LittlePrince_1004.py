T = int(input())

anss = []
for _ in range(T):
  sx, sy, ex, ey = map(int, input().split(' '))

  ans = 0
  N = int(input())
  for _ in range(N):
    x, y, r = map(int, input().split(' '))
    sv = (sx - x) ** 2 + (sy - y) ** 2 - r**2
    ev = (ex - x) ** 2 + (ey - y) ** 2 - r**2
    if sv * ev < 0:
      ans += 1

  anss.append(ans)

for a in anss:
  print(a)
