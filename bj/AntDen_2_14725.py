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

trees = {}
for i in range(N):
  if not trees.get(rows[i][0]):
    trees[rows[i][0]] = {}
  curDict = trees[rows[i][0]]
  for j in range(1, Js[i]):
    if not curDict.get(rows[i][j]):
      curDict[rows[i][j]] = {}
    curDict = curDict[rows[i][j]]

def rec(i, k, children):
  print("--"*i + k)

  for k in sorted(children.keys()):
    rec(i+1, k, children[k])

for k in sorted(trees.keys()):
  rec(0, k, trees[k])