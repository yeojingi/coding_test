N = int(input())
rows = []
for _ in range(N):
  rows.append(list(map(int, list(input()))))

from collections import deque


def zeroOrOne(rows):
  allZero = 1
  allOne = 1
  for row in rows:
    if row.count(0) != len(row):
      allZero = 0
    if row.count(1) != len(row):
      allOne = 0
    if allZero == 0 and allOne == 0:
      return -1

  if allZero == 1:
    return 0
  elif allOne == 1:
    return 1
  return -1

def divideRows(rows):
  row1 = []
  row2 = []
  row3 = []
  row4 = []
  hi = int(len(rows)/2)
  hj = int(len(rows[0])/2)
  for i in range(hi):
    row1.append([])
    row2.append([])
    for j in range(hj):
      row1[i].append(rows[i][j])
    for j in range(hj, hj*2):
      row2[i].append(rows[i][j])

  for i in range(hi, hi*2):
    row3.append([])
    row4.append([])
    for j in range(hj):
      row3[i-hi].append(rows[i][j])
    for j in range(hj, hj*2):
      row4[i-hi].append(rows[i][j])

  return [row1, row2, row3, row4]

def sol(rows):
  c = zeroOrOne(rows)

  if c == 0:
    print(0, end="")
  elif c == 1:
    print(1, end="")
  else:
    print("(", end="")
    nrows = divideRows(rows)
    for nrow in nrows:
      sol(nrow)
    print(")", end="")

sol(rows)
print()