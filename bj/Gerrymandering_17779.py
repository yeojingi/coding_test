import math


N = int(input())

# a, b = 2, 2
# d1, d2 = 1, 2

rows = [list(map(int, input().split(' '))) for _ in range(N)]

ans = math.inf
for a in range(N-2):
  for b in range(1, N-1):
    for d1 in range(1, min(N-a, b+1)):
      for d2 in range(1,N-b):
        sums = [0] * 5
        for x in range(N):
          for y in range(N):
            if (x < a and y < b) or \
              (a <= x <= a + d1 and y < b - (x - a)):
              # rows[y][x] = 1
              sums[0] += rows[y][x]
            elif (a + d1 + d2 < x and y <= b - d1 + d2) or \
              (a + d1 < x <= a + d1 +d2 and y < b - d1 + (x - a - d1)):
              # rows[y][x] = 2
              sums[1] += rows[y][x]
            elif (x < a and y >= b) or \
              (a <= x < a + d2 and y > b + (x - a)):
              # rows[y][x] = 3
              sums[2] += rows[y][x]
            elif (a + d1 + d2 < x and y > b - d1 + d2) or \
              (a + d2 <= x and y > b + d2 - (x - a - d2)):
              # rows[y][x] = 4
              sums[3] += rows[y][x]
            else:
              # rows[y][x] = 5
              sums[4] += rows[y][x]
        ans = min(ans, max(sums) - min(sums))

print(ans)
# for row in rows:
#   print(row)