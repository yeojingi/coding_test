from collections import deque

I, J = map(int, input().split(' '))
rows = []
for _ in range(I):
  rows.append(list(map(int, input().split(' '))))
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

iq = deque([])
for i in range(I):
  for j in range(J):
    if rows[i][j] == 2:
      iq.append([i, j])

def deepcopy(rows):
  nrows = []
  for row in rows:
    nrows.append([*row])

  return nrows

ans = 0
for m in range(I*J):
  i0 = int(m / J)
  j0 = m % J
  if rows[i0][j0] != 0:
    continue
  for n in range(m+1, I*J):
    i1 = int(n / J)
    j1 = n % J
    if rows[i1][j1] != 0:
      continue
    for l in range(n+1, I*J):
      i2 = int(l/J)
      j2 = l % J
      if rows[i2][j2] != 0:
        continue
      nrs = deepcopy(rows)
      nrs[i0][j0] = 1
      nrs[i1][j1] = 1
      nrs[i2][j2] = 1
      # print(f"[{i0}, {j0}] [{i1}, {j1}] [{i2}, {j2}]")

      # for i in range(I):
      #   for j in range(J):
      #     if nrs[i][j] == 2:
      q = deque(iq)

      while q:
        c = q.popleft()
        ci = c[0]
        cj = c[1]

        for k in range(4):
          ni = ci + di[k]
          nj = cj + dj[k]

          if not (ni >= 0 and ni < I and nj >= 0 and nj < J):
            continue

          if nrs[ni][nj] == 0:
            q.append([ni, nj])
            nrs[ni][nj] = 2
        

      tans = 0
      for row in nrs:
        tans += row.count(0)

      # if ans < tans:
      #   print(f"[{i0}, {j0}] [{i1}, {j1}] [{i2}, {j2}] {tans}")
      ans = max(ans, tans)

print(ans)
