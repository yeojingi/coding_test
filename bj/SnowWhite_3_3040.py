from itertools import combinations

dwarfs = [ int(input()) for _ in range(9)]

combs = combinations(dwarfs, 7)

for comb in combs:
  if sum(comb) == 100:
    print(*comb, sep="\n")
    break