matrix = [ list(map(int, input().split())) for _ in range(9) ]

blanks = []
zeros = 0

for i in range(9):
  for j in range(9):

    if matrix[i][j] == 0:
      blanks.append([i, j])
      zeros += 1

def rec(filled):
  global matrix, blanks
  if filled == len(blanks) :
    for row in matrix:
      print(" ".join(list(map(str, row))))
    exit()

  [ci, cj] = blanks[filled]

  for n in range(1, 10):
    n_available = True
    # row check
    for j in range(9):
      if matrix[ci][j] == n:
        n_available = False
        break
    if not n_available:
      continue

    # column check
    for i in range(9):
      if matrix[i][cj] == n:
        n_available = False
        break
    if not n_available:
      continue
  
    # square check  
    for i in range( ci // 3 * 3, ci // 3 * 3 + 3):
      for j in range( cj //3 * 3, cj // 3 * 3 + 3):
        if matrix[i][j] == n:
          n_available = False
          break
      if not n_available:
        break
    if not n_available:
      continue
    
    matrix[ci][cj] = n
    rec(filled+1)
    matrix[ci][cj] = 0

rec(0)