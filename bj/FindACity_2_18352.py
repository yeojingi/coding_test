from collections import deque
import math


N, M, K, X = map(int, input().split(' '))
edges = [[] for _ in range(N+1)]

for _ in range(M):
  [s, e] = list(map(int, input().split(' ')))
  edges[s].append(e)

dp = [ math.inf ] * (N+1)
dp[X] = 0
s = deque()
s.append(X)

while s:
  cur = s.popleft()

  for e in edges[cur]:
    if dp[e] > dp[cur]+1:
      dp[e] = dp[cur]+1
      s.append(e)

isNone = 0
for i in range(N+1):
  if dp[i] == K:
    print(i)
    isNone += 1

if isNone == 0:
  print(-1)