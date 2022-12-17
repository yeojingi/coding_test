import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
matrix = [ list(input()) for _ in range(R) ]

rows = []
elements = {'.': 0, 'S': 1, 'W': 2, 'D': 3}
numToWall = ['.', 'S', 'W', 'D']

sheeps = []

for i in range(R):
  row = []
  for j in range(C):
    row.append( elements[matrix[i][j]] )
    if matrix[i][j] == 'S':
      sheeps.append([i, j])
  rows.append(row)

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

for sheep in sheeps:
  while True:
    q = deque()
    q.append([sheep, [i*C + j]])
    dp = [ [0] * C for _ in range(R) ]

    foundWolf = False

    while q:
      [[ci, cj], track] = q.popleft()
      
      dp[ci][cj] = 1

      if rows[ci][cj] == elements['W']:
        foundWolf = True
        break

      for k in range(4):
        ni = ci + di[k]
        nj = cj + dj[k]

        if not (ni >= 0 and ni < R and nj >= 0 and nj < C):
          continue

        if dp[ni][nj] == 1 or rows[ni][nj] == elements['D']:
          continue
        
        q.append([[ni, nj], track + [ni*C + nj] ])
    
    if not foundWolf:
      break

    installedWall = False
    for cur in track:
      ci = cur // C
      cj = cur % C

      if rows[ci][cj] == elements['.']:
        rows[ci][cj] = elements['D']
        installedWall = True
        break
    
    if not installedWall:
      print(0)
      exit()

print(1)
for i in range(R):
  for j in range(C):
    print(numToWall[ rows[i][j] ], end="")
  print()