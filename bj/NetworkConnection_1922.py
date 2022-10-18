N = int(input())
M = int(input())
edges = [ list(map(int, input().split(' '))) for _ in range(M)]

edges.sort(key=lambda x: x[2])
parents = { i: i  for i in range(1, N+1) }

def findParent(e):
  if parents[e] == e:
    return e
  else:
    return findParent(parents[e])

numEdges = 0
ans = 0
for edge in edges:
  [s, e, d] = edge
  if findParent(s) != findParent(e):
    parents[findParent(e)] = findParent(s)
    ans += d
    numEdges += 1
  if numEdges == N-1:
    break

print(ans)