from tokenize import group


N = int(input())
rows = [ list(map(int, input().split() )) for _ in range(N) ]

tracked = [0] * (2*N-1)
canGo = set([ i for i in range(2*N)])

maxValue = 0

# for d in range(N*2 - 1):
def rec(d, v):
  global maxValue
  if d < N:
    i = N-1 - d
    j = 0
  elif N <= d and d < N*2:
    i = 0
    j = d - (N-1)
  else:
    return

  while i < N and j < N:
    diag = i + j
    if tracked[diag] == 1:
      i += 1
      j += 1
      continue
    if rows[i][j] == 0:
      i += 1
      j += 1
      continue

    tracked[diag] = 1
    rec(d-1, v+1)
    if v+1 > maxValue:
      maxValue = v+1
    tracked[diag] = 0

    i += 1
    j += 1
  rec(d-1, v)

rec(N-1, 0)
print(maxValue)