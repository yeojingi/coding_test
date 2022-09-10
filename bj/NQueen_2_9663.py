N = int(input())
ans = 0
dgs = [0 for _ in range(N)]
# c = 0

def rec(j):
  global ans, dgs, c
  if j == N:
    ans += 1
    return 

  for i in range(N):
    # c+=1
    canPut = True
    for k in range(j):
      dg = dgs[k]
      if i == dg or i - dg == j - k or dg - i == j - k:
        canPut = False
        break
    if canPut:
      dgs[j] = i
      rec(j+1)

rec(0)
print(ans)