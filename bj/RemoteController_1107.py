from collections import deque
import math

# input
goal = int(input())
k = int(input())
if k == 0:
  excs = []
else:
  excs = list(input().split(' '))

ns = list("0123456789")

for exc in excs:
  ns.remove(exc)

# 100
c1 = abs(goal - 100)

# 완전 탐색
prev = [a for a in ns]
ns.append("")

for d in range(1, 6):
  cur = [a for a in prev]
  for ele in prev:
    for a in ns:
      c = int(ele + a)
      cur.append(str(c))
  prev = cur

# print(prev)
c2 = math.inf
for n in prev:
  c = abs(goal-int(n)) + len(n)
  if c2 > c:
    c2 = c
    # print(c, n)

print(min(c1, c2))

# 숫자 부품 하나씩 증가하게 만듦
