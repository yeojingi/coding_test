T = int(input())

def upperbound(arr, v):
  s = 0
  e = len(arr)
  while s < e:
    m = (s + e) // 2
    
    if v <= arr[m]:
      e = m
    else:
      s = m+1
  return s

anss = []
for _ in range(T):
  N, M = map(int, input().split(' '))
  As = list(map(int, input().split(' ')))
  Bs = list(map(int, input().split(' ')))

  Bs.sort()
  ans = 0

  for A in As:
    v = upperbound(Bs, A)
    # print(v, end=" ")
    ans += v
    
  
  anss.append(ans)

print(*anss, sep="\n")