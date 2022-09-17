import math


T = int(input())

anss = []
for _ in range(T):
  N = int(input())
  Hs = list(map(int, input().split()))

  Hs.sort()
  ans = max(abs(Hs[-1] - Hs[-2]) ,abs(Hs[0] - Hs[1]))

  for i in range(N-2):
    ans = max(ans, abs(Hs[i] - Hs[i+2]))
  
  anss.append(ans)

print(*anss, sep="\n")