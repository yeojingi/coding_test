from collections import deque


N, M = map(int, input().split())

rows = [ list(input()) for _ in range(N)]

cur = [0, 0]
for i in range(N):
  for j in range(M):
    if rows[i][j] == '0':
      ci = i
      cj = j

dp = [ [[0]*64 for _ in range(M)] for _ in range(N) ]
dp = [ [ [0] * M for _ in range(N) ] for _ in range(64) ]
dp[0][ci][cj] = 1
key = 0

q = deque()
q.append([ci, cj, 0])

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

keys = set(['a', 'b', 'c', 'd', 'e', 'f'])
doors = set(['A', 'B', 'C', 'D', 'E', 'F'])


while q:
  [ci, cj, ckey] = q.popleft()
  d = dp[ckey][ci][cj]
  
  nkey = ckey
  for k in range(4):
    ni = ci + di[k]
    nj = cj + dj[k]
    # print(ci, cj, ckey, ni, nj, rows[ni][nj])

    if not (ni >= 0 and ni < N and nj >= 0 and nj < M):
      continue
  
    if dp[ckey][ni][nj] != 0:
      continue

    if rows[ni][nj] in keys:
      nkey = ckey | 2**(ord(rows[ni][nj])-97)
      # print(2**(ord(rows[ni][nj])-97))
      
      dp[nkey][ni][nj] = d+1
      q.append([ni, nj, nkey])
    elif rows[ni][nj] in doors:
      if ckey & 2**(ord(rows[ni][nj]) - 65) != 0:
        dp[ckey][ni][nj] = d+1
        q.append([ni, nj, ckey])
    elif rows[ni][nj] == '1':
      # print(*dp, sep="\n")
      print(d)
      exit()
    elif rows[ni][nj] != '#':
      dp[ckey][ni][nj] = d+1
      q.append([ni, nj, ckey])

print(-1)