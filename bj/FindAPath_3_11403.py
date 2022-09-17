N = int(input())
rows = [list(map(int, input().split(' '))) for _ in range(N)]

for k in range(N):
  for i in range(N):
    for j in range(N):
      if rows[i][j] == 0:
        rows[i][j] = rows[i][k] * rows[k][j]

for row in rows:
  print(*row)