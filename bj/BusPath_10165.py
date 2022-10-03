N = int(input())
M = int(input())
paths = []

dict = {}

for i in range(M):
  path = list(map(int, input().split(' ')))

  if path[0] > path[1]:
    path[1] += N

  dict[' '.join(list(map(str, path)))] = i+1
  
  paths.append(path)

paths.sort(key=lambda x: x[0])

dp = [1] * M
cover = [0, 0]
ans = M
for i in range(M):
  if dp[i] == 0:
    continue

  path = paths[i]
  
  j = i

  while True:
    j = (j + 1) % M
    if i == j:
      break

    if dp[j] == 0:
      continue

    cpath = [0, 0]

    if path[1] < N:
      cpath = paths[j]
    else:
      if paths[j][0] < path[0]:
        cpath[0] = paths[j][0] + N
      else:
        cpath[0] = paths[j][0]

      if paths[j][1] < path[0]:
        cpath[1] = paths[j][1] + N
      else:
        cpath[1] = paths[j][1]

    if (path[0] <= cpath[0] and cpath[0] < path[1]) and \
      (path[0] < cpath[1] and cpath[1] <= path[1]):
      dp[j] = 0
    elif path[1] < cpath[0]:
      break
    # print(i, j, path, cpath, dp[j])

anss = []
for i in range(len(dp)):
  if dp[i] == 1:
    anss.append(dict[' '.join(list(map(str, paths[i])))])

anss.sort()
print(' '.join(list(map(str, anss))))

