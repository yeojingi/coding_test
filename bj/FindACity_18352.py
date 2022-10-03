from collections import deque

[N, E, K, S] = list(map(int, input().split(' ')))
Es = [[] for _ in range(N+1)]
for _ in range(E):
  [s, d] = list(map(int, input().split(' ')))
  Es[s].append(d)

visited = [ [0] for _ in  range(N+1)]
visited[S] = 1
to = deque([S])
ds = [0] * (N+1)
Ks = []

while len(to) > 0:
  cur = to.popleft()
  curD = ds[cur]
  # print(cur, curD)

  # process
  if curD == K:
    Ks.append(cur)
  # elif curD > K:
  #   break

  for next in Es[cur]:
    if visited[next] == 1:
      continue
      
    visited[next] = 1
    to.append(next)
    ds[next] = curD+1
  
if len(Ks) == 0:
  print(-1)
  exit()
Ks.sort()
for k in Ks:
  print(k)
