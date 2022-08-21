import math

# input
goal = int(input())
k = int(input())
if k == 0:
  excs = []
else:
  excs = list(map(int, input().split(' ')))

a = list(map(int, "0123456789"))

for exc in excs:
  a.remove(exc)

# 100
c1 = abs(goal - 100)

# 완전 탐색
tg = goal
c2 = 0
while True:
  ttg = tg

  isLtg = True
  while ttg > 0:
    d = ttg % 10
    ttg = int (ttg/ 10)

    if d not in a:
      isLtg = False
      break

  if isLtg == True or tg < 0:
    c2 = goal - tg + len(str(tg))
    break
  
  tg -= 1


tg = goal
c3 = 0
while True:
  ttg = tg
  isLtg = True
  while ttg > 0:
    d = ttg % 10
    ttg = int (ttg/ 10)
    
    if d not in a:
      isLtg = False
      break

  if isLtg:
    c3 = tg - goal + len(str(tg))
    break  
  
  tg += 1

print(min(c1, c2, c3))

# 이건 또 시간이 오래 걸린대 ㅎㅎ