import math
from queue import PriorityQueue
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
edges = [[] for _ in range(V)]

for _ in range(E):
  s, e, d = map(int, input().split())
  s -= 1
  e -= 1

  edges[s].append([e, d])
  edges[e].append([s, d])

formerStartingPoint = -1
q = PriorityQueue()
# dp = PriorityQueue()

q.put((0, 0))
startingPoint = 0

# print(edges)

while True:
  dist = 0
  dp = [math.inf] * V
  dp[startingPoint] = 0 

  while not q.empty():
    [cd, cur] = q.get()
    # print(cur, dp)

    if cd > dp[cur]:
      continue

    for edge in edges[cur]:
      [e, d] = edge
      # print(e, d)

      if dp[e] > dp[cur] + d:
        dp[e] = dp[cur] + d
        q.put((dp[e], e))

  maxDist = dp[0]
  maxI = 0
  for i in range(V):
    if maxDist < dp[i]:
      maxDist = dp[i]
      maxI = i

  endPoint = maxI
  if formerStartingPoint == endPoint:
    break
  else:
    q = PriorityQueue()
    q.put((0, endPoint))
    formerStartingPoint = startingPoint
    startingPoint = endPoint

print(maxDist)