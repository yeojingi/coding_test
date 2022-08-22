from collections import deque

[I, J] = list(map(int, input().split(' ')))
rows = []
for _ in range(I):
  rows.append(list(map(int, list(input()))))

to = deque([[0, 0]])
rows[0][0] = -1
d = deque([1])

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

while len(to) > 0:
  [ci, cj] = to.popleft()
  curD = d.popleft()
  # print(ci, cj)

  for k in range(4):
    ni = ci + di[k]
    nj = cj + dj[k]

    if not (ni >= 0 and ni < I and nj >= 0 and nj < J):
      continue

    if rows[ni][nj] == 1:
      to.append([ni, nj])
      d.append(curD+1)
      rows[ni][nj] = -1
    
    if ni == I-1 and nj == J-1:
      print(curD+1)
      # for row in rows:
      #   print(' '.join(list(map(str, row))))
      exit()
