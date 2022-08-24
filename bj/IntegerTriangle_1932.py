N = int(input())
rows = []

for _ in range(N):
  rows.append([0] + list(map(int, input().split(' '))) + [0])

# print(rows)
for i in range(1, N):
  for j in range(1, i+2):
    rows[i][j] = rows[i][j] + max(rows[i-1][j-1], rows[i-1][j])

# print(rows)
print(max(rows[len(rows)-1]))