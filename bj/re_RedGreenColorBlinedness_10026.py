from copy import deepcopy

N = int(input())
rows = []

def colorMatch(str):
  colorMap = {"R": -1, "G": -2, "B": -3}
  return colorMap[str]

for _ in range(N):
  rows.append(list(map(colorMatch, list(input()))))

rows2 = deepcopy(rows)

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

count = 0
visited = [[False] * N for _ in range(N)]
for i in range(N):
  for j in range(N):
    if visited[i][j] == True:
      continue
  
    if rows[i][j] < 0:
      q = [[i, j]]
      visited[i][j] = True
      count += 1
      color = rows[i][j]

      while q:
        [ci, cj] = q.pop()
        rows[ci][cj] = count

        for k in range(4):
          ni = ci + di[k]
          nj = cj + dj[k]

          if not (ni >= 0 and ni < N and nj >= 0 and nj < N):
            continue
            
          if visited[ni][nj] == False and rows[ni][nj] == color:
            q.append([ni, nj])
            visited[ni][nj] = True


count2 = 0
visited = [[False] * N for _ in range(N)]
for i in range(N):
  for j in range(N):
    if visited[i][j] == True:
      continue
  
    if rows2[i][j] < 0:
      q = [[i, j]]
      visited[i][j] = True
      count2 += 1
      color = rows2[i][j]

      while q:
        [ci, cj] = q.pop()
        rows[ci][cj] = count2

        for k in range(4):
          ni = ci + di[k]
          nj = cj + dj[k]

          if not (ni >= 0 and ni < N and nj >= 0 and nj < N):
            continue
            
          if visited[ni][nj] == False and (rows2[ni][nj] == color or (rows2[ni][nj] == -2 and color == -1) or (rows2[ni][nj] == -1 and color == -2)) :
            q.append([ni, nj])
            visited[ni][nj] = True

print(count, count2)