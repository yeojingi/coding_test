from queue import PriorityQueue

N = int(input())
alphabets = [0] * 26

inputs = []
for _ in range(N):
  s = list(input())
  inputs.append(s)
  i = len(s)-1
  f = 1
  while i >= 0:
    alphabets[ord(s[i]) - 65] += f
    i -= 1
    f *= 10

q = PriorityQueue()
k = 0
j = 0
while k < 26:
  if alphabets[k] == 0:
    k += 1
    continue
  q.put((alphabets[k], k))
  k += 1
  j += 1

i = 10-j
while not q.empty():
  c = q.get()
  alphabets[c[1]] = i
  i += 1

newS = []
for s in inputs:
  cur = ""
  for m in s:
    cur += str(alphabets[ord(m) - 65])
  newS.append(int(cur))

print(sum(newS))