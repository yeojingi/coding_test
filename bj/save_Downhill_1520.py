[N, M] = list(map(int, input().split(' ')))

m = []
for i in range(0, N):
  m.append( list(map(int, input().split(' '))))

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

toVisit = []
answer = 0
cal = 0

def search(i, j):
  ch = m[i][j]
  global answer
  global cal
  cal += 1

  if i == N-1 and j == M-1:
    answer += 1
    return 0

  for k in range(0, 4):
    if not (i+di[k] >= 0 and i+di[k] < N and j+dj[k] >= 0 and j+dj[k] < M):
      continue
    
    if m[i+di[k]][j+dj[k]] < ch:
      search(i+di[k], j+dj[k])

search(0, 0)
print(answer)
print(cal)

# 재귀가 너무 깊다는 에러
# 배열 사용하는 걸로 바꿔보려고 함

# https://www.acmicpc.net/board/view/85228
# 입력때문에 recursion error가 나는 것은 아닙니다.

# python의 기본 재귀 깊이가 1000으로 설정돼 있기 때문에 (그 이상은 RecursionError를 raise합니다) setrecursionlimit()으로 설정해주면 됩니다.

# 이 문제는 입력이 많은 줄로 이루어져 있어 sys.stdin.readline으로 입력을 받아들이면 훨씬 빠르게 입력받을 수 있습니다. 별개의 문제입니다.

# ================================

# 모두 다 탐색헀는지 어떻게 알까?
# 아무데도 갈 곳이 없을 때

# 일단 완전 탐색으로 생각해보면
# 

# =================================

# TypeError: 'list' object is not callable
# 이 에러가 자꾸 생기던데 변수명에 map을 써서 그럼
# 그런데 map 때문이라고 말을 안해주네.
# map이 함수가 사라져서 이상한 값이 돌아갔는데 그걸 list가 처리 못해줬다고 말하는 거구만

