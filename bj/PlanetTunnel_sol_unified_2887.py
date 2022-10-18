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

def findParent(d):
  global heads

  while True:
    if heads[d] == d:
      return d
    
    d = heads[d]

# print(edges)
# 크루스칼 진행
parents = [i for i in range(N)]
cnt,ans = N-1,0
while cnt:
    (w,a,b) = ds.get()
    A = findParent(a)
    B = findParent(b)
    if A == B:
        continue
    heads[B] = A
    cnt-=1
    ans+=w

# print(parents)
print(ans)