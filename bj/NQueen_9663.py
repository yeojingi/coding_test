N = int(input())
ans = 0
dgs = []
c = 0

def rec(j):
  global ans, dgs, c
  if j == N:
    ans += 1
    return 

  Is = [1 for i in range(N)]

  for dg in dgs:
    Is[dg[0]] = 0
    d = j - dg[1]
    if dg[0] - d >= 0:
      Is[dg[0] - d] = 0
    if dg[0] + d < N:
      Is[dg[0] + d] = 0

  for i in range(N):
    if Is[i] == 1:
      dgs.append([i, j])
      rec(j+1)
      dgs.pop()
      
  
  # for i in range(N):
  #   c+=1
  #   canPut = True
  #   for dg in dgs:
  #     if i == dg[0]:
  #       canPut = False
  #       break
  #     elif abs( i - dg[0]) == j - dg[1]:
  #       canPut = False
  #       break
  #   if canPut:
  #     dgs.append([i, j])
  #     rec(j+1)
  #     dgs.pop()

rec(0)
print(ans,c)