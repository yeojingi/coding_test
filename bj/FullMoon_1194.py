from collections import deque


N, M = map(int, input().split(' '))
rows = [ list(input()) for _ in range(N) ]

visited = [ [ [0] * M for __ in range(N)] for _ in range(64)]

keyMask = { chr(ord('a') + i) : 2**i for i in range(6) }
gateMask = { chr(ord('A') + i) : 2** i for i in range(6) }

startPoint = []
for i in range(N):
  for j in range(M):
    if rows[i][j] == '0':
      startPoint = [i, j]

q = deque()
q.append([ *startPoint, 0 ])
visited[0][startPoint[0]][startPoint[1]] = 0
isArrived = -1

# print(rows)

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

while q:
  [ci, cj, cm] = q.popleft()
  # print(ci, cj, cm)
  nm = cm
  
  cd = visited[cm][ci][cj]
  cv = rows[ci][cj]

  if ord('a') <= ord(cv) and ord(cv) <= ord('f'):
    nm = cm | keyMask[cv]
  
  for k in range(4):
    ni = ci + di[k]
    nj = cj + dj[k]

    if not (ni >= 0 and ni < N and nj >= 0 and nj < M):
      continue

    nv = rows[ni][nj]

    if visited[nm][ni][nj] != 0:
      continue
    if nv == '#':
      continue
    elif nv == '1':
      isArrived = cd + 1
      break
    elif ord('A') <= ord(nv) and ord(nv) <= ord('F'):
      if gateMask[nv] & nm != 0:
        q.append([ni, nj, nm])
        visited[nm][ni][nj] = cd + 1
    else:
      q.append([ni, nj, nm])
      visited[nm][ni][nj] = cd + 1
  
  if isArrived != -1:
    break

print(isArrived)