N = int(input())

arrs = []
for _ in range(N):
  arrs.append(list(input()))

for arr in arrs:
  s = []
  for c in arr:
    if c == '(':
      s.append(0)
    else:
      if len(s) > 0:
        s.pop()
      else:
        s.append(3)
        break
  if len(s) > 0:
    print('NO')
  else:
    print('YES')
