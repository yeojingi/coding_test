from math import *

def solution(s):
  m = 100
  for i in range(int(floor(len(s)/2)), len(s)):
    cur = 0
    cura = 100
    while True:
      if i+cur >= len(s):
        cura = i * 2 + 1
        break
      if s[i-cur] != s[i+cur]:
        break
      cur += 1
    m = min(m, cura)
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

# abba 와 같은 케이스를 놓침
# acbca 와 같은 홀수 케이스만 다룸
# 짝수 케이스와 홀수 케이스가 다르다는 것을 못 파악했다