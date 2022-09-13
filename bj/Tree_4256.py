T = int(input())

anss = []
ans = []
tree = []

def rec(cur):
  global ans, tree
  for a in tree[cur]:
    rec(a)
  if cur != 0:
    ans.append(cur)

for _ in range(T):
  N = int(input())
  preOrder = list(map(int, input().strip().split(' ')))
  inOrder = list(map(int, input().strip().split(' ')))
  tree = [[] for _ in range(N+1)]

  traversed = [0] * (N+1)
  head = 0

  pi = 0
  ii = 0
  while ii < N or pi < N:
    curInOrder = inOrder[ii]
    if traversed[curInOrder] == 1:
      head = inOrder[ii]
      ii += 1
    else:
      suf = preOrder[pi]

      tree[head].append(suf)
      traversed[suf] = 1
      head = suf

      pi += 1

  ans = []
  rec(0)
  anss.append(ans)

for a in anss:
  print(" ".join(list(map(str, a))))