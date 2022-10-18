from collections import deque
import copy

N = int(input())
rows = []

def colorMatch(str):
  colorMap = {'R': -1, 'G': -2, 'B': -3}
  return colorMap[str]
for _ in range(N):
  rows.append(list(map(colorMatch, input())))

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

rows2 = copy.deepcopy(rows)

count = 0
for i in range(N):
  for j in range(N):
    if rows[i][j] < 0:
      q = deque([[i, j]])
      count += 1
      color = rows[i][j]
      rows[i][j] = count

      while q:
        [ci, cj] = q.popleft()

        for k in range(4):
          ni = ci + di[k]
          nj = cj + dj[k]

          if not (ni >= 0 and ni < N and nj >= 0 and nj < N):
            continue
          
          if rows[ni][nj] == color:
            q.append([ni, nj])
            rows[ni][nj] = count

count2 = 0
for i in range(N):
  for j in range(N):
    if rows2[i][j] < 0:
      q = deque([[i, j]])
      count2 += 1
      color = rows2[i][j]
      rows2[i][j] = count2

      while q:
        [ci, cj] = q.popleft()

        for k in range(4):
          ni = ci + di[k]
          nj = cj + dj[k]

          if not (ni >= 0 and ni < N and nj >= 0 and nj < N):
            continue
          
          # print(color, rows2[ni][nj], ni, nj)
          if rows2[ni][nj] == color or (color == -1 and rows2[ni][nj] == -2) or (color == -2 and rows2[ni][nj] == -1):
            q.append([ni, nj])
            rows2[ni][nj] = count

print(count, count2)