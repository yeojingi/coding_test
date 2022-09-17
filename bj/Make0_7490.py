from itertools import permutations, product


T = int(input())
opers = ['+', '-', ' ']
anss = []
for _ in range(T):
  N = int(input())
  stack = []
  s = list(product(opers, repeat=N-1))
  datas = []

  for ops in s:
    i = 1
    res = str(1)
    for op in ops:
      i += 1
      res += op + str(i)
    datas.append(res)

  for data in datas:
    a = 0
    b = 0
    po = ''
    for c in data:
      if c == '+' or c == '-':
        if po == '+':
          a += int(b)
          b = 0
        elif po == '-':
          a -= int(b)
          b = 0
        po = c
      elif c == ' ':
        b *= 10
      else:
        b += int(c)
    
    if po == '+':
      a += int(b)
      b = 0
    elif po == '-':
      a -= int(b)
      b = 0
    print(data, a)

  # print(res)