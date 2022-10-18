import math

# initiate
N = int(input())
matrix = [[0] * N for i in range(0, N)]

for i in range(N):
  row = list(map(int, input().split(' ')))
  row = row[1:-1]
  for j in range(0, len(row), 2):
    matrix[i][row[j] - 1] = row[j+1]

v = [False] * N
def search(n):
  v[n] = True
  global N
  ret = 0

  for i in range(0, N):
    if matrix[n][i] != 0 and v[i] == False:
      ret = max(ret, matrix[n][i] + search(i))
  
  v[n] = False
  return ret

ans = math.inf
for i in range(N):
  ans = min(search(i), ans)

print(ans)


# 220816 
# 30분 넘김
# 다익스트라 쓰고 싶었음
# 그래프 탐색이 잘 안 와닿는다
# DFS라는 거 백준에 안 쓰여있었으면 힘들었을 듯
# 거리를 구할 때는 DFS를 쓴다는 것
# 사실 DFS로 거리 구하는 예제를 해본 적이 없어서 겁을 좀 먹었다

# 2D 배열 만드는 법 봐봐
# math.inf로 무한대도 만들 수 있다

# 2D 메트릭스로 표현하면 메모리 초과됨
# 메모리는 256 MB ~= 256 * 10^6 ~= 10^8
# 100,000 * 100,000 배열은 ~= 10^10