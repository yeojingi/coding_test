N, M = map(int, input().split(' '))

picks = []

def rec(N, m, k, p):
  global picks
  
  if m == 0:
    picks.append(p)
    return
  
  for i in range(k+1, N+1):
    if i in p:
      continue
    rec(N, m-1, i, p + [i])

rec(N, M, 0, [])

for pick in picks:
  print(" ".join(list(map(str, pick))))