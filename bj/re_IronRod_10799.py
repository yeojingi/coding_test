arr = list(input())

stack = []
ans = 0
for i in range(len(arr)):
  if arr[i] == '(':
    stack.append(i)
  else:
    c = stack.pop()
    if c == i-1:
      ans += len(stack)
    else:
      ans += 1

print(ans)