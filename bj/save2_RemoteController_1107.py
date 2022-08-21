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

digit = len(str(goal)) - 1
base = len(a)

def decTo(B, i):
  global a
  if i < B:
    return a[i]

  return decTo(B, int(i / B)) * 10 + a[i % B]
print(a)
# brute
ans = math.inf
for i in range(0, base ** (digit+1)):
  t = decTo(base, i)
  
  now = len(str(t)) + abs(t - goal)
  if ans > now:
    ans = now
  print(i, t, len(str(t)), abs(t-goal), now, goal, ans)
  if t == 22:
    print(i, t, len(str(t)), abs(t-goal), now, goal, ans)

# 100
candidate100 = abs(goal - 100)

print(min(ans, candidate100))

# 19
# 2
# 1 0

# 에러
# 22를 못 만듦
# 00이 없기 때문
# 9 -> 00 이 되어야 하는데.

# 각 문자 하나씩 뽑을 때 0이 굉장히 이상하게 작동한다
# 이상한 동작이 뭔데? -> 생각해보자

# 없는 상태 와 0번째 문자 상태를 표현하는 데에 힘들다
# '비어있다' 라는 상태가 하나 더있는데, 이것은 숫자로 표현이 되질 않는다. 숫자에서도 없음으로 표현이 되는데

# 예를 들어,
# 1 이면, 01인데
# 0번째 문자 | 1번째 문자
# 가 아니라,
# 1번째 문자
# 가 표시되어야 함.
# 이것도 기본적으로 그래프 탐색을 해야겠구만

# 그리고 수학 문제 풀 때처럼
# 망한 풀이 중간부터 고쳐가면서 하면 반드시 실수한다는 것 기억해라