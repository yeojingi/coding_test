N = int(input())


for i in range(N):
  for j in range(N):
    t = 1
    isFlag = True
    while t <= i and t <= j:
      if ((i // t)%3 == 1) and ((j // t)%3 == 1):
        print(' ', end = '')
        isFlag = False
        break
      t *= 3
    if isFlag:
      print("*", end="")
  print()