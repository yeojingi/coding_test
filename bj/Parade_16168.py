import sys

input = sys.stdin.readline

V, E = map(int, input().split())
edges = [ [] for _ in range(V+1)]

for i in range(E):
  s, e = map(int, input().split())
  edges[s].append([e, i])
  edges[e].append([s, i])

dp_v = [0] * (V+1)
dp_v[0] = 1
dp_e = [0] * E

s = 1
for i in range(1, V+1):
  if len(edges[i]) % 2 == 1:
    s = i
    break

def rec(n):
  global dp_v, dp_e

  moved = False
  for edge in edges[n]:
    [next, i] = edge

    if dp_e[i] == 1:
      continue

    moved = True
    
    dp_e[i] = 1
    dp_v[next] += 1
    rec(next)
    dp_v[next] -= 1
    dp_e[i] = 0

  if not moved:
    if sum(dp_e) != E:
      return

    for v in range(1, V+1):
      if dp_v[v] == 0:
        return
    
    print("YES")
    exit()

dp_v[s] += 1
rec(s)
print("NO")