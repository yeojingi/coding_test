N, M = map(int, input().split(' '))

ans = []

def rec(l, k, arr):
  if l == 0:
    ans.append(" ".join(list(map(str, list(arr)))))
    return
  
  if k+1> N:
    return 

  for i in range(k+1, N+1):
    rec(l-1, i, arr + [i])

rec(M, 0, [])

for ele in ans:
  print(ele)