import math


V = int(input())
edges = [ [] for _ in range(V+1)]

for _ in range(V):
  edge = list(map(int, input().split(' ')))
  s = edge[0]
  for i in range(1, len(edge) - 2, 2):
    edges[s].append([edge[i], edge[i+1]])

startS = 1
prevS = math.inf
ans = 0
while True:
  dip = [math.inf] * (V+1)
  dip[startS] = 0
  isChanged = False
  v = [startS]
  while v:
    # print(s, dip, v)
    s = v.pop()

    for edge in edges[s]:
      e = edge[0]
      d = edge[1]
      nd = dip[s] + d

      if dip[e] > nd:
        dip[e] = nd
        v.append(e)
        isChanged = True
    if not isChanged:
      break

  maxValue = 0
  arrS = 0
  for i in range(1, V+1):
    if maxValue < dip[i]:
      arrS = i
      maxValue = dip[i]

  # print(prevS, arrS, startS, dip)
  if prevS != arrS:
    prevS = startS
    startS = arrS
  else:
    ans = dip[s]
    break
  # input()

print(max(dip[1:]))