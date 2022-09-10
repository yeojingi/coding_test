N, M = map(int, input().split(' '))

ans = []

def rec(m, picked):
  global N
  if m == 0:
    ans.append(picked)
    return

  for i in range(1, N+1):
    if i not in picked:
      rec(m-1, picked + [i])

rec(M, [])
for a in ans:
  print(" ".join(list(map(str, a))))