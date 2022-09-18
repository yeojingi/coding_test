from re import I


N = int(input())

for ri in range(N):
  row = ""
  for j in range(N):
    i = ri
    output = '*'
    while i > 0 and j > 0:
      if i%3 == 1 and j%3 == 1:
        output = ' '
        break

      i //= 3
      j //= 3
    row += output
  print(row)