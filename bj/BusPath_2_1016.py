N = int(input())
M = int(input())
paths = []

dict = {}

for i in range(M):
  path = list(map(int, input().split(' ')))
  
  paths.append(path)
  dict[' '.join(list(map(str, path)))] = i+1


dp = [1] * M

anss = []
for i in range(M):
  path = paths[i]

  isAdded = True
  toRemove = []
  for j in anss:
    [a, b] = paths[j]
    [c, d] = path

    if a < b and c < d:
      if a <= c and d <= b:
        isAdded = False
      elif c <= a and b <= d:
        toRemove.append(j)
    elif a > b and c < d:
      if a <= c or d <= b:
        isAdded = False
    elif a < b and c > d:
      if c <= a or b <= d:
        toRemove.append(j)
    elif a > b and c > d:
      if a <= c and d <= b:
        isAdded = False
      elif c <= a and b <= d:
        toRemove.append(j)

  while toRemove:
    anss.remove(toRemove.pop())
  if isAdded:
    anss.append(i)

print(" ".join(list(map(lambda x: str(x+1), anss))))