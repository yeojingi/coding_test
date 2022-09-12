T = int(input())
anss = []
for _ in range(T):
  R, N = map(int, input().split(' '))
  ants = [int(input()) for _ in range(N)]
  
  s = 0
  l = 0
  for ant in ants:
    ss = min(ant, R - ant)
    ll = max(ant, R - ant)

    s = max(s, ss)
    l = max(l, ll)
  anss.append(str(s) + ' ' + str(l))

for ans in anss:
  print(ans)