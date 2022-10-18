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

# 좌표를 x,y,z 별로 저장하고 정렬
n = int(input())
xlst,ylst,zlst = [],[],[]
for i in range(n):
    x,y,z = map(int,input().split())
    xlst.append([x,i])
    ylst.append([y,i])
    zlst.append([z,i])
xlst.sort(key = lambda x: x[0]); ylst.sort(key = lambda x: x[0]); zlst.sort(key = lambda x: x[0])

Xds = []
Yds = []
Zds = []

for i in range(n-1):
  Xds.append([xlst[i+1][0] - xlst[i][0], xlst[i][1], xlst[i+1][1]])
  Yds.append([ylst[i+1][0] - ylst[i][0], ylst[i][1], ylst[i+1][1]])
  Zds.append([zlst[i+1][0] - zlst[i][0], zlst[i][1], zlst[i+1][1]])

numEdges = 0

Xds.sort(key=lambda x: x[0])
Yds.sort(key=lambda x: x[0])
Zds.sort(key=lambda x: x[0])

# 인접한 행성들끼리 간선 구성

edges = PriorityQueue()

for Xd in Xds:
  edges.put(tuple(Xd))
for Yd in Yds:
  edges.put(tuple(Yd))
for Zd in Zds:
  edges.put(tuple(Zd))

# edges.sort(reverse=True)

# print(edges)
# 크루스칼 진행
parents = [i for i in range(n)]
cnt,ans = n-1,0

# Priority Queue도 되는데요?

while cnt:
    w,a,b = edges.get()
    A = find(a)
    B = find(b)
    if A == B:
        continue
    parents[B] = A
    cnt-=1
    ans+=w

# print(parents)
print(ans)