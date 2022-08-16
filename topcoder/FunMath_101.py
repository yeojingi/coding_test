# 220815

def solution(base):
  answer = []
  for i in range(1, base):
    if base % i == 1:
      answer.append(i)
  return answer


assert solution(10) == [3, 9], solution(10)
assert solution(3) == [2], solution(3)
assert solution(9) == [2, 4, 8], solution(9)
assert solution(26) == [5, 25], solution(26)
assert solution(30) == [29], solution(30)