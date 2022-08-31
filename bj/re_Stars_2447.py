from wsgiref.handlers import IISCGIHandler


N = int(input())

for ii in range(N):
  for ij in range(N):
    flag = False
    i = ii
    j = ij
    while i > 0 and j > 0:
      if i % 3 == 1 and j % 3 == 1:
        print(' ', end='')
        flag = True
        break
      i = i // 3
      j = j // 3
    if flag == False:
      print('*', end='')
  print()
      