s = input()
d = s[0]
ans = 0
p = d
for k in s:
  if k != p:
    if k != d:
      ans += 1
    p = k
print(ans)