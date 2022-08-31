N = int(input())
rows = [['*'] * N for _ in range(N)]

def sol(si, ei, sj, ej):
  d = (ei - si) // 3
  li = si + d
  ri = li + d
  lj = sj + d
  rj = lj + d

  for i in range(li, ri):
    for j in range(lj, rj):
      rows[i][j] = ' '
  
  if d > 1:
    sol(si, li, sj, lj)
    sol(si, li, lj, rj)
    sol(si, li, rj, ej)
    sol(li, ri, sj, lj)

    sol(li, ri, rj, ej)
    sol(ri, ei, sj, lj)
    sol(ri, ei, lj, rj)
    sol(ri, ei, rj, ej)

sol(0, N, 0, N)
for row in rows:
  print(''.join(row))