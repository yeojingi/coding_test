def bisect(iter, h, s, e):
  if s >= e:
    return e
  
  m = s + (e - s) // 2
  
  if h < iter[m][0]:
    e = m - 1
  elif h > iter[m][0]:
    s = m + 1
  else:
    return -2

  return bisect(iter, h, s, e)

N = int(input())
seq = list(map(int, input().split(' ')))

dp = [[seq[0], 1]]
for i in range(1, N):
  a = bisect(dp, seq[i], 0, len(dp))
  if a == -2:
    continue
  elif a < 0 or a >= len(dp):
    dp.append([seq[i], 1])
    dp.sort(key=lambda x: x[0])
  else:
    dp[a][1] += 1
  print(seq[i], dp, a)