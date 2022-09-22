T = int(input())

anss = []
for _ in range(T):
  string = input()
  series = 0
  ans = 0
  for c in string:
    if c == 'X':
      series = 0
    else:
      series += 1
      ans += series
  anss.append(ans)

print(*anss, sep="\n")