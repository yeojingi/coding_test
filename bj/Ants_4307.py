T = int(input())
ans = []
for _ in range(T):
  L, N = map(int, input().split(' '))
  shortest = 0
  longest = 0
  for __ in range(N):
    h = int(input())
    if h > L-h:
      shortest = max(shortest, L-h)
      longest = max(longest, h)
    else:
      shortest = max(shortest, h)
      longest = max(longest, L-h)
  ans.append([shortest, longest])

for a in ans:
  print(a[0], a[1])