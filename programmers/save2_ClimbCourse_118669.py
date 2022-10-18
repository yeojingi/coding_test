from collections import deque
import math

def solution(n, paths, gates, summits):
  answer = [math.inf, math.inf]
  npaths = [[] for _ in range(n+1)]
  
  for path in paths:
    npaths[path[0]].append([path[1], path[2]])
    npaths[path[1]].append([path[0], path[2]])

  summits.reverse()
  # print(npaths)
  
  for summit in summits:
    dist = [math.inf] * (n+1)
    v = [False] * (n+1)
    
    for edge in npaths[summit]:
      dist[edge[0]] = edge[1]
    
    for _ in range(n-2):
      mval = math.inf
      cur = 0
      for i in range(1, n+1):
        if dist[i] <= mval and v[i] == False:
          cur = i
          mval = dist[i]
      # print(cur, summit, dist)
      v[cur] = True
      
      if cur in gates:
        if answer[1] >= dist[cur]:
          answer[0] = summit
          answer[1] = dist[cur]
        break
      
      for edge in npaths[cur]:
        next = edge[0]
        if next in summits:
          continue
        d = max(edge[1], dist[cur])
        dist[next] = min(d, dist[next])
  
  return answer

print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))