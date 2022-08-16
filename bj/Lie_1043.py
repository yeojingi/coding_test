def solution(N, nP, Ts, Ps):
  visited = [False] * (N+1)
  canAttend = [1] * nP
  toVisit = []

  for T in Ts:
    visited[T] = True
    toVisit.append(T)

  while len(toVisit) > 0:
    v = toVisit.pop()
    for i in range(0, nP):
      if canAttend[i] == 0:
        continue

      if v in Ps[i]:
        canAttend[i] = 0
        
        for delegate in Ps[i]:
          if visited[delegate] == False:
            visited[delegate] = True
            toVisit.append(delegate)
          
        

  return sum(canAttend)

[N, P] = list(map(int, input().split(' ')))
T = list(map(int, input().split(' ')))
I = T[0]
Ts = T[1:]

Ps = []
for i in range(0, P):
  aP = list(map(int, input().split(' ')))
  if aP[0] == 0:
    aP = []
  else:
    aP = aP[1:]
  Ps.append(aP)


print(solution(N, P, Ts, Ps))
