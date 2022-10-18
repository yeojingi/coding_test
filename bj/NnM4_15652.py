N, M = map(int, input().split(' '))

anss = []
def rec(i, ans):
  if len(ans) >= M-1:
    anss.append(ans+ str(i))
    return 

  for j in range(i, N+1):
    rec(j, ans + str(i))

for i in range(1, N+1):
  rec(i, "")
for ans in anss:
  print(' '.join(ans))