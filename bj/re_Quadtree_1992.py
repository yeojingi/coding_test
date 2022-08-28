N = int(input())
rows = []
for _ in range(N):
  rows.append(list(map(int, list(input()))))

ans = ""

def sol(si, ei, sj, ej):
  global ans
  flag = True
  cr = rows[si][sj]
  for i in range(si, ei):
    for j in range(sj, ej):

      if rows[i][j] != cr:
        flag = False
        break
    if flag == False:
      break
  
  if flag == False:
    ans += '('
    mi = (si+ei)//2
    mj = (sj+ej)//2
    sol(si, mi, sj, mj)
    sol(si, mi, mj, ej)
    sol(mi, ei, sj, mj)
    sol(mi, ei, mj, ej)
    ans += ')'
  else:
    ans += str(cr)

sol(0, N, 0, N)
print(ans)