N = int(input())
rows = [list(map(int, input().split(' '))) for _ in range(N)]

whites = 0
blues = 0

def rec(si, ei, sj, ej):
  global rows, whites, blues
  d = rows[si][sj]

  flag = True
  for i in range(si, ei):
    for j in range(sj, ej):
      if d != rows[i][j]:
        flag = False
        break
    if not flag:
      break
  
  if flag:
    if d == 0:
      whites += 1
    elif d == 1:
      blues += 1
  else:
    mi = si + (ei - si) // 2
    mj = sj + (ej - sj) // 2
    rec(si, mi, sj, mj)
    rec(mi, ei, sj, mj)
    rec(si, mi, mj, ej)
    rec(mi, ei, mj, ej)

rec(0, N, 0, N)
print(whites)
print(blues)