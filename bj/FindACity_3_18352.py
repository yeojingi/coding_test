import math
from queue import PriorityQueue
from collections import deque

N, M, K, X = map(int, input().split())

# edges = [ list(map(int, input().split())) + [m] for m in range(M) ]
edges = [ [] for _ in range(N+1) ]

for m in range(M):
  s, e = map(int, input().split())
  edges[s].append([e, m])

dp = [math.inf] * (N+1)
# dpEdgeInStack = [0] * M

q = deque()
s = X
q.append(s)
dp[s] = 0

# print(edges)
while q:
  cur = q.popleft()
  d = dp[cur]

  for edge in edges[cur]:
    [e, i] = edge

    if dp[e] > d + 1:
      dp[e] = d+1
      q.append(e)

# print(dp)

found = False
for i in range(1, N+1):
  if dp[i] == K:
    print(i)
    found = True

if not found:
  print(-1)
