import math


N = int(input())
row = list(map(int, input().split(' ')))

row.sort()
area = row[-1] * row[-2]
area += row[0] * row[1]
for i in range(2, N):
  area += row[i] * row[i-2]

area = area / 2 * math.sin(math.pi * 2 / N)
print("%.3f"%area)