N = int(input())
matrix = [[] for _ in range(N+1)]
for _ in range(N-1):
  a, b = map(int, input().split(' '))
  matrix[a].append(b)
  matrix[b].append(a)

s = [1]
ans = [0] * (N+1)

# print(matrix)
while s:
  cur = s.pop()

  for next in matrix[cur]:
    if ans[next] == 0:
      s.append(next)
      ans[next] = cur

for i in range(2, N+1):
  print(ans[i])
