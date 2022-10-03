negative_che = set()
che = []

for i in range(2, 10000):
  if i not in negative_che:
    che.append(i)
  elif i in negative_che:
    continue

  j = i*2
  while j <= 10000:
    negative_che.add(j)
    j += i

T = int(input())
anss = []
for _ in range(T):
  I = int(input())
  for i in range(I // 2, I):
    if i in che and I - i in che:
      anss.append(f"{I-i} {i}")
      break

print("\n".join(anss))