from collections import deque
import math
from queue import PriorityQueue


N = int(input())
Xs = PriorityQueue()
Ys = PriorityQueue()
Zs = PriorityQueue()
heads = [ i for i in range(N) ]

# 3N
for i in range(N):
  coord = list(map(int, input().split(' ')))
  Xs.put((coord[0], i))
  Ys.put((coord[1], i))
  Zs.put((coord[2], i))

Xds = PriorityQueue()
Yds = PriorityQueue()
Zds = PriorityQueue()

pX = Xs.get()
pY = Ys.get()
pZ = Zs.get()

for i in range(1, N):
  nX = Xs.get()
  nY = Ys.get()
  nZ = Zs.get()

  Xds.put([nX[0] - pX[0], pX[1], nX[1]])
  Yds.put([nY[0] - pY[0], pY[1], nY[1]])
  Zds.put([nZ[0] - pZ[0], pZ[1], nZ[1]])

  pX = nX
  pY = nY
  pZ = nZ

numEdges = 0

ds = PriorityQueue()

while not Xds.empty():
  Xd = Xds.get()
  ds.put(Xd)

while not Yds.empty():
  Yd = Yds.get()
  ds.put(Yd)

while not Zds.empty():
  Zd = Zds.get()
  ds.put(Zd)

def findParent(x):
    if x != heads[x]:
        heads[x] = findParent(heads[x])
    return heads[x]

# def findParent(d):
#   global heads

#   while True:
#     if heads[d] == d:
#       return d
    
#     d = heads[d]
  

expense = 0
while numEdges < N-1:
  [d, f, t] = ds.get()
  # print(d, f, t)

  hf = findParent(f)
  ht = findParent(t)

  if hf != ht:
    # print(numEdges, expense, '|', d, '|', f, t, '|', hf, ht, heads)
    heads[ht] = hf
    expense += d
    numEdges += 1

# print(heads)
print(expense)