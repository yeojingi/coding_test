s = input()

stack = []
ans = 0
for i in range(len(s)):
  if s[i] == ')':
    d = stack.pop()
    if d == i -1:
      ans += len(stack)
    else:
      ans += 1
  else:
    stack.append(i)

print(ans)