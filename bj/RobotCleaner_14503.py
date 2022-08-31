N, M = map(int, input().split(' '))
ri, rj, d = map(int, input().split(' '))
rows = []
for _ in range(N):
  rows.append( list(map(int, input().split(' '))))

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

ans = 0
while True:
  if rows[ri][rj] == 0:
    rows[ri][rj] = 2
    ans += 1

  left = 1 # 0: 갈 공간이 있다 | 1: 벽이다
  all = 1 # 0: 갈 공간이 있다 | 1: 갈 공간이 없다
  behind = 0 # 0: 벽은 아니다 | 1: 벽이다

  for k in range(4):
    td = (d + 3*k) % 4
    ti = ri + di[td]
    tj = rj + dj[td]

    # if not (ti >= 0 and ti < N and tj >= 0 and tj < M):
    #   continue

    if k == 1:
      left = rows[ti][tj]
    if rows[ti][tj] == 0:
      all = 0
    if k == 2:
      behind = rows[ti][tj]

  
  if left == 0:
    d = (d + 3) % 4
    ri = ri + di[d]
    rj = rj + dj[d]
    continue
  if all == 1 and behind == 1:
    break
  elif all == 1 and behind != 1:
    td = (d+2)%4
    ri = ri + di[td]
    rj = rj + dj[td]
    continue
  d = (d+3)%4
  
print(ans)
