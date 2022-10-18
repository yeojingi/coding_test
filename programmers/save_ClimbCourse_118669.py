from collections import deque
import math

def solution(n, paths, gates, summits):
  answer = [math.inf, math.inf]
  npaths = [[] for _ in range(n+1)]
  
  for path in paths:
    npaths[path[0]].append([path[1], path[2]])
    npaths[path[1]].append([path[0], path[2]])

  # print(npaths)
  summits.sort()
  
  dist = [0] * (n+1)
  for summit in summits:
    q = deque([summit])
    
    while q:
      cur = q.popleft()
      
      for edge in npaths[cur]:
        next = edge[0]
        d = max(edge[1], dist[cur])
        
        if next in summits:
          continue
        if next in gates:
          if answer[1] > d:
            answer[1] = d
            answer[0] = summit
          continue
        elif dist[next] != 0 and d < dist[next]:
          dist[next] = d
          q.append(next)
        elif dist[next] == 0:
          dist[next] = d
          q.append(next)
  
  return answer

print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))