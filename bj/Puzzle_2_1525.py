from collections import deque

been = set()
q = deque()

# rows = [ input().split() for _ in range(3) ]

s = ""
for _ in range(3):
  s += "".join(input().split())

been.add(s)
q.append([s, 0])

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

while q:
  [cur, d] = q.popleft()
  for cp in range(9):
    if cur[cp] == '0':
      break

  if cur == "123456780":
    print(d)
    exit()
  
  ci = cp // 3
  cj = cp % 3

  for k in range(4):
    ni = ci + di[k]
    nj = cj + dj[k]

    if not (ni >= 0 and ni < 3 and nj >= 0 and nj < 3):
      continue

    np = ni * 3 + nj
    
    ns = ""

    for l in range(9):
      if l == np:
        ns += cur[cp]
      elif l == cp:
        ns += cur[np]
      else:
        ns += cur[l]
    
    if ns not in been:
      been.add(ns)
      q.append([ns, d+1])


print(-1)