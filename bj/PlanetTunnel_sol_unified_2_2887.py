from queue import PriorityQueue
import sys
input = sys.stdin.readline

def union(x,y):
    x = find(x)
    y = find(y)
    parents[y] = x

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

# 좌표를 x,y,z 별로 저장하고 정렬
n = int(input())
xlst,ylst,zlst = PriorityQueue(), PriorityQueue(), PriorityQueue()

# 3N
for i in range(n):
  coord = list(map(int, input().split(' ')))
  xlst.put((coord[0], i))
  ylst.put((coord[1], i))
  zlst.put((coord[2], i))

# 인접한 행성들끼리 간선 구성
edges = []
for curList in xlst,ylst,zlst:
    for i in range(1,n):
        w1,a = curList[i-1]
        w2,b = curList[i]
        edges.append((abs(w1-w2),a,b))
edges.sort(reverse = True)

# print(edges)
# 크루스칼 진행
parents = [i for i in range(n+1)]
cnt,ans = n-1,0
while cnt:
    w,a,b = edges.pop()
    if find(a) == find(b):
        continue
    union(a,b)
    cnt-=1
    ans+=w

# print(parents)
print(ans)