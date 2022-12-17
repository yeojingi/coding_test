import sys

input = sys.stdin.readline

V, E = map(int, input().split())
edges = [ [] for _ in range(V+1)]

for i in range(E):
  s, e = map(int, input().split())
  edges[s].append([e, i])
  edges[e].append([s, i])

dp_e = [0] * E

s = []
circuit = []
numEdge = 0

cur = 1

numOdd = 0 
for i in range(1, V+1):
  if len(edges[i]) % 2 == 1:
    cur = i
    numOdd += 1

if not (numOdd == 0 or numOdd == 2):
  print("NO")
  exit()

while numEdge < E:
  hasEdge = False

  for edge in edges[cur]:
    [e, i] = edge

    if dp_e[i] == 1:
      continue

    hasEdge = True
    s.append(cur)
    cur = e
    dp_e[i] = 1
    break

  if not hasEdge:
    if s:
      cur = s.pop()
    else:
      break
    numEdge += 1
    circuit.append(cur)


if numEdge == E:
  print("YES")
else:
  print("NO")