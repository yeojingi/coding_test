from collections import deque
import math
from queue import PriorityQueue

import sys
input = sys.stdin.readline

N = int(input())
coords = []
Xs = []
Ys = []
Zs = []
heads = [ i for i in range(N) ]

for i in range(N):
  coord = list(map(int, input().split(' ')))
  Xs.append([ coord[0], i ])
  Ys.append([ coord[1], i ])
  Zs.append([ coord[2], i ])

Xs.sort(key=lambda x: x[0])
Ys.sort(key=lambda x: x[0])
Zs.sort(key=lambda x: x[0])

Xds = []
Yds = []
Zds = []

for i in range(N-1):
  Xds.append([Xs[i+1][0] - Xs[i][0], Xs[i][1], Xs[i+1][1]])
  Yds.append([Ys[i+1][0] - Ys[i][0], Ys[i][1], Ys[i+1][1]])
  Zds.append([Zs[i+1][0] - Zs[i][0], Zs[i][1], Zs[i+1][1]])

numEdges = 0

Xds.sort(key=lambda x: x[0])
Yds.sort(key=lambda x: x[0])
Zds.sort(key=lambda x: x[0])

# ds = deque()

# x = 0
# y = 0
# z = 0
# for i in range((N-1) * 3):
#   which = 0
#   d = math.inf

#   if x < N-1 and Xds[x][0] < d:
#     d = Xds[x][0]
#     which = 0
#   if y < N-1 and Yds[y][0] < d:
#     d = Yds[y][0]
#     which = 1
#   if z < N-1 and Zds[z][0] < d:
#     d = Zds[z][0]
#     which = 2

#   if which == 0:
#     ds.append(Xds[x])
#     x += 1
#   elif which == 1:
#     ds.append(Yds[y])
#     y += 1
#   elif which == 2:
#     ds.append(Zds[z])
#     z += 1

ds = PriorityQueue()

for Xd in Xds:
  ds.put(tuple(Xd))
for Yd in Yds:
  ds.put(tuple(Yd))
for Zd in Zds:
  ds.put(tuple(Zd))

def findParent(x):
    if x != heads[x]:
        heads[x] = findParent(heads[x])
    return heads[x]
  

expense = 0
while ds and numEdges < N-1:
  [d, f, t] = ds.get()

  hf = findParent(f)
  ht = findParent(t)

  if hf != ht:
    # print(numEdges, expense, d, f, t, hf, ht, heads)
    heads[ht] = hf
    expense += d
    numEdges += 1

print(expense)