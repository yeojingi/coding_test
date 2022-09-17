N = int(input())

rows = []
for _ in range(N):
  rows.append(list(map(int, input().split(' '))))

def sp(i, j, k):
  return max(rows[i][j], rows[i][k] * rows[k][j])

for k in range(N):
  for i in range(N):
    for j in range(N):
      rows[i][j] = sp(i, j, k)

for row in rows:
  print(" ".join(list(map(str, list(row)))))