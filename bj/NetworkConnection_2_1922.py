N = int(input())
M = int(input())
edges = [ list(map(int, input().split(' '))) for _ in range(M)]

parents = [ i for i in range(N+1) ]

def findParent(n):
  while n != parents[n]:
    n = parents[n]
  
  return n

edges.sort(key=lambda x: x[2])
edges.reverse()
numEdges = 0
expense = 0

while numEdges < N-1:
  [s, e, d] = edges.pop()

  ps = findParent(s)
  pe = findParent(e)

  if ps == pe:
    continue

  parents[ps] = pe
  numEdges += 1
  expense += d

print(expense)