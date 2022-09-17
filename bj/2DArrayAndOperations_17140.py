from queue import PriorityQueue


def operation(list):
  result = []
  q = PriorityQueue()
  m = {}

  for e in list:
    if e == 0:
      continue
    if not m.get(e):
      m[e] = 1
    else:
      m[e] += 1

  for key, value in m.items():
    q.put((value, key))

  val = PriorityQueue()
  fre = 0
  while not q.empty():
    e = q.get()
    if fre != e[0]:
      while not val.empty():
        result.append(val.get())
        result.append(fre)
      val = PriorityQueue()
      fre = e[0]
    val.put(e[1])
  
  while not val.empty():
    result.append(val.get())
    result.append(fre)

  return result

r, c, k = map(int, input().split(' '))
rows = [list(map(int, input().split(' '))) for _ in range(3)]
n = 0

while n <= 100:
  R = len(rows)
  C = len(rows[0])

  if r-1 < len(rows) and c-1 < len(rows[0]) and rows[r-1][c-1] == k:
    break

  if R >= C:
    newRows = []
    maxLength = 0
    for row in rows:
      newRow = operation(row)
      if len(newRow) > maxLength:
        maxLength = len(newRow)
      newRows.append(newRow)
    
    for i in range(len(newRows)):
      while len(newRows[i]) < maxLength:
        newRows[i].append(0)

    rows = newRows

  elif R < C:
    newRows = []
    maxLength = 0
    for i in range(C):
      textRow = [ rows[j][i] for j in range(R) ]
      newRow = operation(textRow)
      if len(newRow) > maxLength:
        maxLength = len(newRow)
      newRows.append(newRow)
    
    for i in range(len(newRows)):
      while len(newRows[i]) < maxLength:
        newRows[i].append(0)

    NR = len(newRows)
    NC = len(newRows[0])
    rows = [ [0] * NR for _ in range(NC)]
    for i in range(NR):
      for j in range(NC):
        rows[j][i] = newRows[i][j]

  n += 1

if n == 101:
  print(-1)
else:
  print(n)