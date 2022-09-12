N = int(input())

rows = []
for _ in range(N):
  rows.append(input())

for row in rows:
  stack = []
  
  for i in range(len(row)):
    if row[i] == '(':
      stack.append(i)
    else:
      if len(stack) > 0:
        stack.pop()
      else:
        stack.append(-1)
        break
  if len(stack) > 0:
    print('NO')
  else:
    print('YES')