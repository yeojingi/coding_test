from math import *

def solution(s):
  m = len(s)
  flag = True
  while flag:
    f = 0
    b = m-1
    flag = False
    while f <= b:
      if b < len(s) and s[f] != s[b]:
          flag = True
      f += 1
      b -= 1
    if flag:
      m += 1
    else:
      return m

params = [
  "abab",
  "abacaba",
  "qwerty",
  "abdfhdyrbdbsdfghjkllkjhgfds"
]
answers = [
  5,
  7,
  11,
  38
]

for i in range(0, len(params)):
  print(params[i])
  assert solution(params[i]) == answers[i], solution(params[i])

# 왜 이건 풀릴까?
# 이 아이디어는 어떻게 떠올렸을까?
