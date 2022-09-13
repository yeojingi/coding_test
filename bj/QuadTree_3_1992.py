N = int(input())
rows = [ list(map(int, list(input()))) for _ in range(N)]

ans = ""
def rec(si, ei, sj, ej):
  global rows, ans
  d = rows[si][sj]

  flag = False
  for i in range(si, ei):
    for j in range(sj, ej):
      if d != rows[i][j]:
        flag = True
        break
    if flag:
      break

  if flag:
    ans += '('
    mi = si + (ei - si) // 2
    mj = sj + (ej - sj) // 2
    rec(si, mi, sj, mj)
    rec(si, mi, mj, ej)
    rec(mi, ei, sj, mj)
    rec(mi, ei, mj, ej)
    ans += ')'
  else:
    ans += str(d)

rec(0, N, 0, N)
print(ans)