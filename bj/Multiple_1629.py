import math

A, B, C = map(int, input().split())

a = A % C

cur = a
res = 1
index = 1

str = "{0:b}".format(B)
# print(str)

while True:
  if index > len(str):
    break

  if str[-index] == '1':
    # print(index-1, math.log(cur) / math.log(A), cur)
    res *= cur
    res %= C

  cur = (cur * cur) % C
  index += 1

print(res)