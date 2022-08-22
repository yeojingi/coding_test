from bisect import *

N = int(input())
Ns = list(map(int, input().split(' ')))
M = int(input())
Ms = list(map(int, input().split(' ')))

Ns.sort()

def bs(s, e, k):
  global Ns

  d = int((s+e)/2)
  if Ns[d] == k:
    return 1
  
  if s == e:
    return 0
  
  if Ns[d] < k:
    return bs(bisect_right(Ns, Ns[d]), e, k)
  else:
    return bs(s, bisect_left(Ns, Ns[d]), k)

for i in range(0, M):
  print(bs(0, N-1, Ms[i]))