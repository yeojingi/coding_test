N = int(input())

def alphaToNum(s):
  if s == '.':
    return -1
  return ord(s) - 65

def numToAlpha(n):
  return chr(n+65)

tree = [ [] for _ in range(N) ]
for _ in range(N):
  a = list(map(alphaToNum, input().split(' ')))
  for c in a[1:]:
    tree[a[0]].append(c)

ans = ""
def pre(n):
  global ans, tree
  
  if n == -1:
    return
  
  [a, b] = tree[n]
  ans += numToAlpha(n)
  pre(a)
  pre(b)

def inOrder(n):
  global ans, tree
  
  if n == -1:
    return
  
  [a, b] = tree[n]
  inOrder(a)
  ans += numToAlpha(n)
  inOrder(b)

def inOrderWhile(n):
  global ans, tree
  
  s  = []
  while s or n != -1 : # node != Null은 머임
    if n != -1:
      s.append(n)
      n = tree[n][0]
    else:
      n = s.pop()
      ans += numToAlpha(n)
      n = tree[n][1]

def post(n):
  global ans, tree
  
  if n == -1:
    return
  
  [a, b] = tree[n]
  post(a)
  post(b)
  ans += numToAlpha(n)

def postWhile(n):
  global ans, tree
  s = []
  t = []
  s.append(n)
  while s:
    n = s.pop()
    t.append(n)
    if tree[n][0] != -1:
      s.append(tree[n][0])
    if tree[n][1] != -1:
      s.append(tree[n][1])
  
  while t:
    n = t.pop()
    ans += numToAlpha(n)

pre(0)
print(ans)
ans = ""
inOrder(0)
print(ans)
ans = ""
inOrderWhile(0)
print(ans)
ans = ""
post(0)
print(ans)
ans = ""
postWhile(0)
print(ans)