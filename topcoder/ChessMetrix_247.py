def solution(size, start, end, numMoves):
  di = [1, 1, 1, 0, -1, -1, -1, 0, 2, 1, -1, -2, -2, -1, 1, 2]
  dj = [1, 0, -1, -1, -1, 0, 1, 1, -1, -2, -2, -1, 1, 2, 2, 1]

  mat = [[[0 for j in range(size)] for k in range(size)] for i in range(numMoves+1)]
  mat[0][start[0]][start[1]] = 1

  # print(mat)
  # print(mat[2][1][1])
  for t in range(1, numMoves+1):
    for i in range(0, size):
      for j in range(0, size):

        for k in range(len(di)):
          ni = i + di[k]
          nj = j + dj[k]

          if ni >= 0 and ni < size and nj >= 0 and nj < size:
            # print(ni, nj, t, numMoves)
            mat[t][ni][nj] += mat[t-1][i][j]
          
  # print(mat)
  # print(mat[numMoves][end[0]][end[1]])
  return mat[numMoves][end[0]][end[1]]

assert solution(3, [0, 0], [1, 0], 1) == 1
assert solution(3, [0, 0], [1, 2], 1) == 1
assert solution(3, [0, 0], [2, 2], 1) == 0
assert solution(3, [0, 0], [0, 0], 2) == 5
assert solution(100, [0, 0], [0, 99], 50) == 243097320072600