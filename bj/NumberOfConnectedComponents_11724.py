N, M = map(int, input().split(' '))
Es = [list(map(int, input().split(' '))) for _ in range(M)]
vs = [0] * (N+1)
vs[0] = 0

paths = [ [] for _ in range(N+1) ]
for E in Es:
  paths[E[0]].append(E[1])
  paths[E[1]].append(E[0])

ans = 0
for i in range(1, N+1):
  stack = []
  if vs[i] == 0:
    ans += 1
    stack.append(i)
    vs[i] = ans
    while stack:
      cur = stack.pop()
      
      for way in paths[cur]:
        if vs[way] == 0:
          stack.append(way)
          vs[way] = ans

# print(vs)
print(ans)
