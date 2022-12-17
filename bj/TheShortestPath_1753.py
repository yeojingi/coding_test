import sys
from queue import PriorityQueue
import math

input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())
edges = [ [] for _ in range(V+1) ]
for _ in range(E):
  s, e, w = map(int, input().split())
  edges[s].append([e, w])

dp = [0] * (V+1)
distances = [math.inf] * (V+1)
q = PriorityQueue()
q.put((0, K))
dp[K] = 1
distances[K] = 0

while not q.empty():
  [curD, cur] = list(q.get())

  if dp[cur] == 2:
    continue

  dp[cur] = 2

  nexts = edges[cur]

  for next in nexts:
    [n, d] = next

    if curD + d < distances[n]:
      dp[n] = 1
      distances[n] = curD + d
      q.put((distances[n], n))

for i in range(1, V+1):
  if distances[i] == math.inf:
    print("INF")
  else:
    print(distances[i])