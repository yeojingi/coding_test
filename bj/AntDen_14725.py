# 자료 구조가 완전히 틀려버렸어라~
N = int(input())
rows = []

maxJ = 0
Js = []
for i in range(N):
  [j, *row] = input().split()
  j = int(j)
  Js.append(j)
  if j > maxJ:
    maxJ = j
  rows.append(row)

trees = []
for j in range(maxJ):
  trees.append({})
  for i in range(N):
    if j >= Js[i]:
      continue

    cur = rows[i][j]
    if j == 0:
      if not trees[0].get(cur):
        trees[0][cur] = []
    else:
      parent = rows[i][j-1]
      if cur not in trees[j-1][parent]:
        trees[j-1][parent].append(cur)
      if not trees[j].get(cur):
        trees[j][cur] = []

def rec(j, k):
  if j == maxJ:
    return

  print("--" * j + k)
  children = trees[j][k]
  children.sort()

  for k in children:
    rec(j+1, k)

for k in sorted(trees[0].keys()):
  rec(0, k)