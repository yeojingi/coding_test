N = int(input())
rows = [ list(map(int, input().split(' '))) for _ in range(N) ]

stack = []
circuit = []
v = [0]
visited = [ i for i in range(N)]
numEdges = 0

# - If all vertices have same out-degrees as in-degrees - choose any of them.
# - If all but 2 vertices have same out-degree as in-degree, and one of those 2 vertices has out-degree with one greater than its in-degree, and the other has in-degree with one greater than its out-degree - then choose the vertex that has its out-degree with one greater than its in-degree.
# - Otherwise no euler circuit or path exists.

sums = []
odds = []
for i in range(N):
  value = sum(rows[i])
  if value % 2 == 1:
    odds.append(i)
  sums.append(value)

if len(odds) == 0:
  v = [0]
elif len(odds) == 2:
  v = [odds[0]]
else:
  print(-1)
  exit()

numEdges = sum(sums) // 2

if numEdges == 0:
  print(-1)
  exit()


while numEdges > 0:
  cur = v.pop()
  # print(cur)

  for j in range(N):
    if rows[cur][j] > 0:
      v.append(j)
      rows[cur][j] -= 1
      if cur != j:
        rows[j][cur] -= 1
      numEdges -= 1
      break

  if not v:
    circuit.append(cur)
    for i in range(len(visited)):
      if visited[i] == cur:
        visited.pop(i)
        break
    if len(stack) > 0:
      v.append(stack.pop())
    else:
      break
  else:
    stack.append(cur)

  if not stack and not v:
    break

if v:
  circuit.append(v.pop())

while stack:
  circuit.append(stack.pop())

def toPrint(s):
  return str(s+1)

# print(*rows, sep="\n")

if numEdges > 0 or circuit[0] != circuit[-1]:
  print(-1)
else:
  print(' '.join(list(map(toPrint, circuit))))


