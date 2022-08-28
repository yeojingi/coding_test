arr = list(input())

stack = []
ans = 0
justOpened = False

for c in arr:
  if c == '(':
    stack.append(c)
    justOpened = True
  else:
    if stack and stack[-1] == '(' and justOpened == True:
      stack.pop()
      ans += len(stack)
    elif stack and stack[-1] == '(' and justOpened == False:
      stack.pop()
      ans += 1
    justOpened = False
  # print(c, end="")

print(ans)