from collections import deque
import math
from queue import PriorityQueue
from tracemalloc import start


N = int(input())
edges = [ [] for _ in range(N) ]
for _ in range(N-1):
  [s, e, d] = list(map(int, input().split(' ')))

  edges[s-1].append([e-1, d])
  edges[e-1].append([s-1, d])

startingPoint = 0
formerStartingPoint = -1

while True:
  dp = [math.inf] * N

  dp[startingPoint] = 0
  v = PriorityQueue()
  v.put((0, startingPoint))

  while not v.empty():
    (_, cur) = v.get()
    cd = dp[cur]
    
    for edge in edges[cur]:
      [n, d] = edge
      nd = cd + d

      if dp[n] > nd:
        dp[n] = nd
        v.put((dp[n], n))

  endingPoint = 0
  d = 0
  for i in range(N):
    if d < dp[i]:
      d = dp[i]
      endingPoint = i
  # print(dp)

  if endingPoint == formerStartingPoint:
    print(d)
    exit()
  else:
    formerStartingPoint = startingPoint
    startingPoint = endingPoint