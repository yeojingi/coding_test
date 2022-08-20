from collections import deque

GS = int(input())
gs = deque([])

for i in range(GS):
  gs.append(int(input()))

g = gs.popleft()
w = 1
r = []
stack = []

while True:
  if g < w:
    temp = stack.pop()
    if temp != g:
      print("NO")
      exit()
    else:
      r.append('-')
      if len(gs) == 0:
        break
      g = gs.popleft()
  else:
    r.append('+')
    stack.append(w)
    w += 1

for y in r:
  print(y)