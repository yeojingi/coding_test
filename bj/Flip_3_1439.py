from re import A


s = list(map(int, list(input())))

d = s[0]
i = 0
ans = 0
while i < len(s):
  if d != s[i]:
    ans += 1
    while i < len(s) and d != s[i]:
      i += 1
  i += 1

print(ans)