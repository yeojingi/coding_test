N = int(input())
rows = [input() for _ in range(N)]

anss = []
for row in rows:
  i = 0
  ans = 0
  for c in row:
    if c == 'X':
      i = 0
    else:
      i += 1
      ans += i
  
  anss.append(ans)

print(*anss, sep="\n")