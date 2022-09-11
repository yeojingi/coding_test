from collections import deque

class Node:
  def __init__(self, item):
    self.node = item[0]
    self.left = None
    self.right = None

  def setLeft(self, item):
    self.left = item
  
  def getLeft(self):
    return self.left

  def setRight(self, item):
    self.right = item

  def getRight(self):
    return self.right
  
class Tree:
  def __init__(self):
    self.head = None

def charToInt(item):
  if item == '.':
    return -1
  return ord(item) - 65

def intToChar(item):
  return chr(item + 65)

N = int(input())
trees = [list(map(charToInt, input().split(' '))) for _ in range(N)]
trees.sort(key=lambda x: x[0])

# preorder
ansPre = ""
stack = [0]
while stack:
  cur = stack.pop()
  ansPre += intToChar(cur)
  if trees[cur][2] != -1:
    stack.append(trees[cur][2])
  if trees[cur][1] != -1:
    stack.append(trees[cur][1])

print(ansPre)

# inorder
ansIn = ""

def recInOrder(cur):
  global trees, ansIn

  if trees[cur][1] != -1:
    recInOrder( trees[cur][1] )

  ansIn += intToChar(cur)

  if trees[cur][2] != -1:
    recInOrder( trees[cur][2] )

recInOrder(0)
print(ansIn)


# postorder
ansPost = ""

def recPostOrder(cur):
  global trees, ansPost

  if trees[cur][1] != -1:
    recPostOrder( trees[cur][1] )

  if trees[cur][2] != -1:
    recPostOrder( trees[cur][2] )

  ansPost += intToChar(cur)

recPostOrder(0)
print(ansPost)