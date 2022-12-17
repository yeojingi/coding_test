import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
matrix = [ list(input()) for _ in range(R) ]

rows = []

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

for i in range(R):
  for j in range(C):
    if matrix[i][j] == 'S':
      for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if not (ni >= 0 and ni < R and nj >= 0 and nj < C):
          continue

        if matrix[ni][nj] == 'W':
          print(0)
          exit()
    if matrix[i][j] == '.':
      matrix[i][j] = 'D'

print(1)
for row in matrix:
  print("".join(row), end="")