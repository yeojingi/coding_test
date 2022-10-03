from collections import deque


rows = [ list(input().split(' ')) for _ in range(3) ]

string = ''.join([ ''.join(row)  for row in rows])

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

q = deque()
q.append(string)
visited = {string: 0}
cal = 0

while q:
  cur = q.popleft()
  cal += 1
  # print(cur, cd, cal, visited)

  if cur == '123456780':
    print(visited[cur])
    exit()

  ci, cj = 0, 0
  
  for i in range(3):
    for j in range(3):
      if cur[i*3 + j] == '0':
        ci = i
        cj = j
        break
  
  for k in range(4):
    ni = ci + di[k]
    nj = cj + dj[k]

    if not (ni >= 0 and ni < 3 and nj >= 0 and nj < 3):
      continue

    temp = cur[ni * 3 + nj]

    newString = ""
    for i in range(3):
      for j in range(3):
        if i == ni and j == nj:
          newString += '0'
        elif i == ci and j == cj:
          newString += temp
        else:
          newString += cur[i * 3 + j]
    
    if visited.get(newString):
      continue

    q.append(newString)
    visited[newString] = visited[cur] + 1
print(-1)