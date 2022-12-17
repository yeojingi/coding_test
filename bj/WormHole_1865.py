import sys
input = sys.stdin.readline

T = int(input())

anss = []

def rec(n, t, s):
  global edges_dp

  moved = False

  for edge in edges[n]:
    [e, d, i] = edge

    if edges_dp[i] == 1:
      continue

    moved = True
    if e == s:
      if t+d < 0:
        return True
    
    edges_dp[i] = 1
    found = rec(e, t+d, s)
    if found:
      return True
    edges_dp[i] = 0
  
  if not moved:
    return False

for test in range(T):
  N, M, W = map(int, input().split())
  edges = [ [] for _ in range(N+1) ]
  for i in range(M+W):
    s, e, d = map(int, input().split())
    if i >= M:
      d *= -1

    edges[s].append([e, d, i])
    
  found = False
  for s in range(1, N+1):
    edges_dp = [0] * (M+W)
    found = rec(s, 0, s)
    
    if found:
      anss.append("YES")
      break
  if not found:
    anss.append("NO")

for ans in anss:
  print(ans)
