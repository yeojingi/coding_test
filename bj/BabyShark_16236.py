from collections import deque
from queue import PriorityQueue

N = int(input())
rows = []
startPoint = []

for i in range(N):
  row = list(map(int, input().split(' ')))
  try:
    j = row.index(9)
    startPoint = [i, j]
  except ValueError:
    pass
  rows.append(row)

dp = [ [-1] * N for _ in range(N) ]

q = deque()
nq = PriorityQueue()
q.append([*startPoint, 0, 0])
t = 0
e = 0
d = 0
rows[startPoint[0]][startPoint[1]] = 0
dp[startPoint[0]][startPoint[1]] = e
size = 2

di = [-1, 0, 0, 1]
dj = [0, -1, 1, 0]

while q:
  [ci, cj, ct, ce] = q.popleft()


  if rows[ci][cj] != 0 and rows[ci][cj] < size:
    rows[ci][cj] = 0
    e += 1
    if e >= (size * (size + 1) - 2) // 2:
      size += 1
    q = deque()
    nq = PriorityQueue()
    d = 0
    q.append([ci, cj, ct, e])
    t = ct
    # print(*dp, sep="\n")
    # print(ci, cj, ct, e, size)
    continue

  for k in range(4):
    ni = ci + di[k]
    nj = cj + dj[k]

    if not (ni >= 0 and ni < N and nj >= 0 and nj < N):
      continue

    if dp[ni][nj] != ce and rows[ni][nj] <= size:
      # q.append([ni, nj, ct+1, ce])
      nq.put((ni, [ni, nj, ct+1, ce]))
      dp[ni][nj] = ce

  if not q:
    while not nq.empty():
      ele = nq.get()
      ele = ele[1]
      q.append(ele)
    d += 1

print(t)