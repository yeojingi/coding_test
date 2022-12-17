N = int(input())
matrix = [ list(map(int, input().split())) for _ in range(N) ]
vertical = [ [0] * N for _ in range(N) ]
horizontal = [ [0] * N for _ in range(N) ]
diagonal = [ [0] * N for _ in range(N) ]

horizontal[0][1] = 1

for j in range(N):
  if matrix[0][j] == 1:
    break
  horizontal[0][j] = 1

for j in range(2, N):
  for i in range(1, N):
    if matrix[i][j] == 1:
      continue

    # vertical
    vertical[i][j] = vertical[i-1][j] + diagonal[i-1][j]

    # horizontal
    horizontal[i][j] = diagonal[i][j-1] + horizontal[i][j-1]

    # diagonal
    if matrix[i-1][j] != 1 and matrix[i][j-1] != 1:
      diagonal[i][j] = vertical[i-1][j-1] + horizontal[i-1][j-1] + diagonal[i-1][j-1]

# print("vertical")
# print(*vertical, sep="\n")
# print("horizontal")
# print(*horizontal, sep="\n")
# print("diagonal")
# print(*diagonal, sep="\n")
print( vertical[N-1][N-1] + horizontal[N-1][N-1] + diagonal[N-1][N-1] )