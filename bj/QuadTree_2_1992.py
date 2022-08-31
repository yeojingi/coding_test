N = int(input())
rows = []
for _ in range(N):
  rows.append(list(input()))

def conquer(lu, rd):
  si = lu[0]
  ei = rd[0]
  sj = lu[1]
  ej = rd[1]

  d = rows[si][sj]
  flag = True
  for i in range(si, ei):
    for j in range(sj, ej):
      if rows[i][j] != d:
        flag = False
        break
    if flag == False:
      break

  if flag == False:
    print("(", end="")
    mi = (si + ei) // 2
    mj = (sj + ej) // 2
    conquer([si, sj], [mi, mj])
    conquer([si, mj], [mi, ej])
    conquer([mi, sj], [ei, mj])
    conquer([mi, mj], [ei, ej])
    print(")", end="")
  else:
    print(d, end="")

conquer([0, 0], [N, N])
print()