from itertools import combinations

hats = []
for _ in range(9):
  hats.append(int(input()))

combs = list(combinations(hats, 7))

for comb in combs:
  if sum(comb) == 100:
    for num in comb:
      print(num)
    break