N, M = map(int, input().split(' '))

ans = []
def rec(n, arr):
  if n == 0:
    ans.append(" ".join(map(str, arr)))
    return 
  
  for k in range(1, N+1):
    if k not in arr:
      rec(n-1, arr + [k])

rec(M, [])

for ele in ans:
  print(ele)