N, M = map(int, input().split(' '))
r, c, d = map(int, input().split(' '))
rows = [list(map(int, input().split(' '))) for _ in range(N)]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

ci = r
cj = c
cd = d
ans = 0

while True:
  if rows[ci][cj] == 0:
    rows[ci][cj] = 2
    ans += 1
  
  cantMove = True
  for k in range(4):
    ni = ci + di[k]
    nj = cj + dj[k]

    if not (ni >= 0 and ni < N and nj >= 0 and nj < M):
      continue

    if rows[ni][nj] == 0:
      cantMove = False
      break

  if cantMove:
    bd = (d + 2) % 4
    bi = ci + di[bd]
    bj = cj + dj[bd]

    if rows[bi][bj] == 1:
      break
    elif rows[bi][bj] == 2:
      ci = bi
      cj = bj
  else:
    d = (d + 3) % 4
    ni = ci + di[d]
    nj = cj + dj[d]

    if rows[ni][nj] == 0:
      ci = ni
      cj = nj

print(ans)