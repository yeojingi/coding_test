[N, M] = list(map(int, input().split(' ')))

m = []
for i in range(0, N):
  m.append( list(map(int, input().split(' '))))

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

toVisit = [[0, 0]]
answer = 0
cal = 0

while len(toVisit) > 0:
  v = toVisit.pop()
  i = v[0]
  j = v[1]
  ch = m[i][j]

  if i == N-1 and j == M-1:
    answer += 1
    continue

  for k in range(0, 4):
    if not (i+di[k] >= 0 and i+di[k] < N and j+dj[k] >= 0 and j+dj[k] < M):
      continue
    
    cal += 1
    if m[i+di[k]][j+dj[k]] < ch:
      toVisit.append([i+di[k], j+dj[k]])

print(answer)
print(cal)

# 이번엔 시간 초과?
# 시간 초과가 왜 일어나지? 잘 분리 했는데..?
# 
