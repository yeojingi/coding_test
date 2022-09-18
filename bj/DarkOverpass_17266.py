from math import ceil


N = int(input())
M = int(input())
positions = list(map(int, input().split(' ')))

positions.sort()
ans = 0
for i in range(M):
  value = 0
  if i == 0:
    value = positions[0]
    if ans < value:
      ans = value
  
  if i == M-1:
    value = max(N-positions[i], ceil((positions[i]-positions[i-1])/2))
  else:
    value = ceil((positions[i] - positions[i-1]) / 2)

  if ans < value:
    ans = value

print(ans)

