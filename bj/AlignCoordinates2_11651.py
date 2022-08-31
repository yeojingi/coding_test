from functools import cmp_to_key


N = int(input())
coords = []
for _ in range(N):
  coords.append(list(map(int, input().split(' '))))

def compare(a, b):
  if a[1] == b[1]:
    return a[0] - b[0]
  return a[1] - b[1]

coords.sort(key = cmp_to_key(compare))
for coord in coords:
  print(" ".join(list(map(str, coord))))