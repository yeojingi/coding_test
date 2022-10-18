from collections import deque
import math

def solution(n, paths, gates, summits):
  sp = [ [math.inf] * (n+1) for _ in range(n+1)]

  for path in paths:
    sp[path[0]][path[1]] = path[2]
    sp[path[1]][path[0]] = path[2]

  
  for k in range(1, n+1):
    if k in gates or k in summits:
      continue
    for i in range(1, n+1):
      for j in range(1, n+1):
        sp[i][j] = min(sp[i][j], sp[i][k], sp[k][j])

  for s in sp:
    print(s)
  
  answer = [math.inf, math.inf]
  for gate in gates:
    for summit in summits:
      if answer[1] > sp[gate][summit]:
        answer[1] = sp[gate][summit]
        answer[0] = gate
      elif answer[1] == sp[gate][summit] and answer[0] > gate:
        answer[0] = gate
  
  return answer

print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))