from itertools import combinations

hats = []
for _ in range(9):
  hats.append(int(input()))

cs = combinations(hats, 7)

for c in cs:
  if (sum(c) == 100):
    for k in c:
      print(k)
    break