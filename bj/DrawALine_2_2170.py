N = int(input())
lines = [list(map(int, input().split(' '))) for _ in range(N)]

lines.sort(key=lambda x: x[0])

drawn = []

ans = 0 
for i in range(N):
  line = lines[i]

  if not drawn:
    drawn = line
    continue

  if line[0] <= drawn[1]:
    if line[1] < drawn[1]:
      continue
    elif line[1] > drawn[1]:
      drawn[1] = line[1]
  else:
    ans += drawn[1] - drawn[0]
    drawn = line

ans += drawn[1] - drawn[0]

print(ans)