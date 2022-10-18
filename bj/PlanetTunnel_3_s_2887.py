from queue import PriorityQueue
import sys
input = sys.stdin.readline

def union(x,y):
    x = find(x)
    y = find(y)
    parents[y] = x

def find(x):
    # 이것도 바꾸면 문제 됨
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

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

ds = PriorityQueue()

for Xd in Xds:
  ds.put(tuple(Xd))
for Yd in Yds:
  ds.put(tuple(Yd))
for Zd in Zds:
  ds.put(tuple(Zd))

# edges.sort(reverse=True)

# print(edges)
# 크루스칼 진행
parents = [i for i in range(N)]
expense = 0
numEdges = 0
while numEdges < N-1:
    [d, f, t] = ds.get()
    hf = find(f)
    ht = find(t)
    if hf == ht:
        continue
    parents[ht] = hf
    numEdges += 1
    expense+=d

# print(parents)
print(expense)