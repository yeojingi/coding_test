import sys

input = sys.stdin.readline

V, E = map(int, input().split())
edges = [ list(map(int, input().split())) for _ in range(E) ]
edges.sort(key=lambda x: x[2])

def findParent(x):
  while x != dp[x]:
    x = dp[x]
  return x

dp = [i for i in range(V+1)]

numEdge = 0
sum = 0
for edge in edges:
  [s, e, d] = edge
  # s -= 1
  # e -= 1

  ps = findParent(s)
  pe = findParent(e)

  if ps != pe:
    # 이게 중요하네..?
    if ps > pe:
      dp[ps] = pe
    else:
      dp[pe] = ps
    sum += d
    numEdge += 1
  
  if numEdge == V-1:
    break

# print(dp)
print(sum)