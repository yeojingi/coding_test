import math
import sys
sys.setrecursionlimit(10**6)

# initiate
N = int(input())
matrix = [[]]

for i in range(N):
  row = list(map(int, input().split(' ')))
  row = row[1:-1]
  matrix.append(row)

def dfs(n):
  v = [False] * (N+1)
  v[n] = True
  to = [n]
  d = [0] * (N+1)

  while len(to) > 0:
    cur = to.pop()

    for i in range(0, len(matrix[cur]), 2):
      next = matrix[cur][i]
      dist = matrix[cur][i+1]
      
      if v[next] == False:
        v[next] = True
        to.append(next)

        if d[next] < d[cur] + dist:
          d[next] = d[cur] + dist
  
  dist = max(d)
  far = d.index(dist)

  return [dist, far]

ans = 0
# for i in range(1, N+1):
#   ans = max(search(i, 0), ans)

d = 0
f = 1
sf = 1
while True:
  [d, nf] = dfs(f)
  # print(nf, sf)
  if nf == sf:
    print(d)
    break
  sf = f
  f = nf

# print(ans[0])


# 220816 
# 220822
# 수학이 들어가네.. ㅋㅋㅋㅋ
# 그리고 재귀 함수로 DFS 짠 게 이미 잘못임
# 아니네 이건 기억해야 하는 게 있어서 재귀를 써야 하나..?