V, E = map(int, input().split())
edges = [ list(map(int, input().split())) for _ in range(E) ]

parent = [ i for i in range(V+1) ]

def findParent(x):
  while x != parent[x]:
    x = parent[x]
  
  return x

edges.sort(key= lambda x: x[2])
numEdge = 0
sumWeight = 0

for edge in edges:
  [s, e, d] = edge
  ps = findParent(s)
  pe = findParent(e)

  if ps < pe:
    parent[ps] = pe
    numEdge += 1
    sumWeight += d
  elif ps > pe:
    parent[pe] = ps
    numEdge += 1
    sumWeight += d

  if numEdge == E-1:
    break

print(sumWeight)