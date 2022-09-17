import math
from queue import PriorityQueue


N, M, X = map(int, input().split(' '))
paths = [ [] for _ in range(N+1)]
rpaths = [ [] for _ in range(N+1)]

for _ in range(M):
  s, e, t = map(int, input().split(' '))
  paths[s].append([e, t])
  rpaths[e].append([s, t])

revdist = [0] * (N+1)
dist = [0] * (N+1)

for i in range(1, N+1):
  dp = [math.inf] * (N+1)
  rdp = [math.inf] * (N+1)

  q = PriorityQueue()
  for path in paths[i]:
    e = path[0]
    t = path[1]
    dp[e] = t
    q.put([t, e])

  rq = PriorityQueue()
  for path in rpaths[i]:
    e = path[0]
    t = path[1]
    rdp[e] = t
    rq.put([t, e])

  while not q.empty():
    [curT, curI] = q.get()
    
    if dp[curI] < curT:
      continue

    for path in paths[curI]:
      e = path[0]
      t = path[1]
      if dp[e] > dp[curI] + t:
        dp[e] = dp[curI] + t
        q.put([dp[e], e])
  print(dp)