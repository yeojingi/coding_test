from itertools import permutations, product


T = int(input())
opers = [' ', '+', '-']
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
    processedData = data.replace(' ', '')

    sum = 0
    a = ""
    po = '+'
    for i in range(len(processedData)):
      if processedData[i] == '+' or processedData[i] == '-':
        if po == '+':
          sum += int(a)
        elif po == '-':
          sum -= int(a)
          
        po = processedData[i]
        a = ""
      else:
        a += processedData[i]
    if po == '+':
      sum += int(a)
    elif po == '-':
      sum -= int(a)

    # print(data, sum)
    if sum == 0:
      anss.append(data)
  
  
  anss.append(' ')
  # print(res)
for ans in anss[:-1]:
  print(ans)