N = int(input())
rows = []
for _ in range(N):
  rows.append(list(map(int, input().split(' '))))
ones = 0
zeros = 0

def rec(ul, dr):
  global zeros, ones
  ui = ul[0]
  lj = ul[1]
  di = dr[0]
  rj = dr[1]

  d = rows[ui][lj]
  sameFlag = True
  for i in range(ui, di):
    for j in range(lj, rj):
      if d != rows[i][j]:
        sameFlag = False
        break
    if not sameFlag:
      break

  if sameFlag:
    if d == 1:
      ones += 1
    else:
      zeros += 1
    return
  
  mi = ui + (di - ui) // 2
  mj = lj + (rj - lj) // 2
  rec([ui, lj], [mi, mj])
  rec([ui, mj], [mi, rj])
  rec([mi, lj], [di, mj])
  rec([mi, mj], [di, rj])

rec([0, 0,], [N, N])
print(zeros)
print(ones)