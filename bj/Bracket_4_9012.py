N = int(input())
cases = [ list(input()) for _ in range(N) ]
ans = []
for case in cases:
  s = []
  for i in range(len(case)):
    if case[i] == '(':
      s.append(i)
    else:
      if s:
        s.pop()
      else:
        s.append(-1)
        break
  
  if len(s) > 0:
    ans.append("NO")
  else:
    ans.append("YES")

for a in ans:
  print(a)