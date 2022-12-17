from copy import deepcopy

def mark(mi, mj, k, rows):
  new_rows = deepcopy(rows)

  for i in range(9):
    new_rows[i][mj] |=  2 ** (k - 1)
  for j in range(9):
    new_rows[mi][j] |= 2 ** (k - 1)
  
  cell_i = mi // 3
  cell_j = mj // 3

  for i in range(cell_i * 3, cell_i * 3 + 3):
    for j in range(cell_j * 3, cell_j * 3 + 3):
      new_rows[i][j] |= 2 ** (k - 1)
  
  return new_rows

input_rows = [ list(map(int, list(input()))) for _ in range(9) ]
rows = [ [0] * 9 for _ in range(9) ]

for i in range(9):
  for j in range(9):
    k = input_rows[i][j]
    if k != 0:
      rows = mark(i, j, k, rows)

print(*rows, sep="\n")

one_missings = [510, 509, 507, 503, 495, 479, 447, 383, 255]
t = 0
while True:
  no_change = True
  print(t)
  for i in range(9):
    for j in range(9):
      if rows[i][j] in one_missings:
        num = one_missings.index(rows[i][j]) + 1
        rows = mark(i, j, num, rows)
        input_rows[i][j] = num
    if not no_change:
      break
  if no_change:
    break
  t += 1
print(*input_rows, sep="\n")