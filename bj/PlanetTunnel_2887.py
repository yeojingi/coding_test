N = int(input())
coords = []
Xs = []
Ys = []
Zs = []

for i in range(N):
  coord = list(map(int, input().split(' ')))
  coords.append([ *coord, i ])
  Xs.append([ *coord, i ])
  Ys.append([ *coord, i ])
  Zs.append([ *coord, i ])

Xs.sort(key=lambda x: x[0])
Ys.sort(key=lambda x: x[1])
Zs.sort(key=lambda x: x[2])

numEdges = 0