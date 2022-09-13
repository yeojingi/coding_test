from queue import PriorityQueue

N, M = map(int, input().split(' '))
infos = [list(map(int, input().split(' '))) for _ in range(M)]
dp = [0] * (N+1)
routes = [[] for _ in range(N+1)]

for info in infos:
  dp[info[1]] += 1
  routes[info[0]].append(info[1])

toVisit = PriorityQueue()
for i in range(1, N+1):
  if dp[i] == 0:
    toVisit.put(i)
    dp[i] -= 1

ans = ""
while not toVisit.empty():
  cur = toVisit.get()

  ans += str(cur) + " "

  routes[cur].sort()
  for n in routes[cur]:
    if dp[n] > 0:
      dp[n] -= 1
      if dp[n] == 0:
        toVisit.put(n)
print(ans[:-1])