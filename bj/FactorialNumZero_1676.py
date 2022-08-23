import math

N = int(input())

def insu(k, l):
  ans = 0

  while True:
    temp = k % l
    if temp == 0:
      ans += 1
      k = int(k / l)
    else:
      break

  return [k, ans]

a = [0, 0, 0]

for k in range(1, N+1):
  i = k
  [k, n2] = insu(k ,2)
  [_, n5] = insu(k, 5)
  a[0] = a[0] + (n2 - n5)
  a[1] = 0
  a[2] = a[2] + n5

print(a[2])