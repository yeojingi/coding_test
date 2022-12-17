matrix = [ list(map(int, input().split())) for _ in range(9)]
N = 9

squares = [ [ set([i for i in range(1, 10)]) for _ in range(3) ] for _ in range(3) ]
columns = [ set([i for i in range(1, 10)]) for _ in range(N) ]
rows = [ set([i for i in range(1, 10)]) for _ in range(N) ]
zeros = 9*9

def note_down(i, j, n):
  global columns, squares, rows, zeros
  columns[j].remove(n)
  rows[i].remove(n)
  squares[ i // 3 ][ j // 3 ].remove(n)
  matrix[i][j] = n
  zeros -= 1

def note_up(i, j, n):
  global columns, squares, rows, zeros
  columns[j].add(n)
  rows[i].add(n)
  squares[ i // 3 ][ j // 3 ].add(n)
  matrix[i][j] = 0
  zeros += 1

for i in range(N):
  for j in range(N):
    if matrix[i][j] != 0:
      note_down(i, j, matrix[i][j])

def rec(i, startJ):
  if zeros == 0:
    for r in matrix:
      print(" ".join(list(map(str, r))))
    exit()
    
  if i >= 9:
    return

  for j in range(startJ, 9):
    if matrix[i][j] != 0:
      continue
    
    row = list(rows[i])
    for n in row:
      if n in columns[j] and n in squares[ i//3 ][ j//3 ]:
        note_down(i, j, n)
        if len(rows[i]) == 0:
          rec(i+1, 0)
        else:
          rec(i, j+1)
        note_up(i, j, n)

rec(0, 0)