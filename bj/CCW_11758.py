coords = [list(map(int, input().split(' '))) for _ in range(3)]

d1 = [ coords[1][0] - coords[0][0], coords[1][1] - coords[0][1]]
d2 = [ coords[2][0] - coords[1][0], coords[2][1] - coords[1][1]]

res = d1[0] * d2[1] - d1[1] * d2[0]

if res == 0:
  print(0)
elif res < 0:
  print(-1)
elif res > 0:
  print(1)