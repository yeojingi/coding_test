expression = input()

Operators = ['+', '-', '*', '/', '(', ')']

vals = []
ops = []

for c in expression:
  if c in Operators:
    if c in ['+', '-']:
      while ops and ops[-1] != '(':
        vals.append(ops.pop())
      ops.append(c)
    elif c in ['*', '/']:
      if ops and ops[-1] in ['*', '/']:
        vals.append(ops.pop())
      ops.append(c)
    elif c == '(':
      ops.append(c)
    elif c == ')':
      while ops:
        cur = ops.pop()
        if cur == '(':
          break
        vals.append(cur)
  else:
    vals.append(c)

while ops:
  vals.append(ops.pop())

print("".join(vals))
