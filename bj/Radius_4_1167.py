import math
from queue import PriorityQueue


N = int(input())
edges = [ [] for _ in range(N+1) ]

for _ in range(N):
  stream = list(map(int, input().split(' ')))
  index = stream[0]
  for i in range(1, len(stream)-1, 2):
    edges[index].append([stream[i], stream[i+1]])

formerStartPoint = 1
currentStartPoint = 1
while True:

  dp = [math.inf] * (N+1)
  dp[currentStartPoint] = 0

  q = PriorityQueue()
  q.put((0, currentStartPoint))

  while not q.empty():
    cur = q.get()[1]  
    # print(cur)
    
    adjacents = edges[cur]
    for edge in adjacents:
      e = edge[0]
      d = edge[1]
      if dp[e] > dp[cur] + d:
        dp[e] = dp[cur] + d
        q.put((dp[e], e))
  # print(dp)

  maxIndex = 1
  maxValue = 0
  for i in range(1, N+1):
    if dp[i] > maxValue:
      maxIndex = i
      maxValue = dp[i]

  if formerStartPoint == maxIndex:
    # print(formerStartPoint, maxIndex, maxValue)
    print(maxValue)
    break

  formerStartPoint = currentStartPoint
  currentStartPoint = maxIndex