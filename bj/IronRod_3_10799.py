s = list(input())

t = []
ans = 0
for i in range(len(s)):
  if s[i] == '(':
    t.append(i)
  elif s[i] == ')':
    c = t.pop()
    if c == i-1:
      ans += len(t)
    else:
      ans += 1

print(ans)