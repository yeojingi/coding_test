from collections import deque

# input
goal = int(input())
k = int(input())
if k == 0:
  excs = []
else:
  excs = list(input().split(' '))

a = list("0123456789")

for exc in excs:
  a.remove(exc)

# 100
c1 = abs(goal - 100)

# 완전 탐색
words = []
lower = True

words = deque([e for e in a])
if '0' in words:
  words.remove('0')
isLower = True
c2 = 0
c3 = 0

while len(words) > 0:
  word = words.popleft()


  if int(word) >= goal and isLower == True:
    c3 = int(word) - goal + len(str(word))
    # print(word, c2, c3)
    break
  
  c2 = goal - int(word) + len(str(word))
  # print(word, 'fd', c2)

  for e in a:
    words.append(word + e)
  

if c2 == 0 and c3 == 0:
  c3= c2 = goal+1


# print(min(c1, c2, c3), c1, c2, c3)
print(min(c1, c2, c3))

# 숫자에서는 0이 앞에 나올 수 없다는 것!