from email import header


expression = input()

class Tree:
  def __init__(self, item) -> None:
    self.arr = [[item, None, None]]
    self.head = 0
    self.tail = 0

  def addToHead(self, val1, val2):
    self.arr.append([val1, self.head, val2])
    self.head = len(self.arr)-1

  def addToTail(self, val1, val2):
    self.arr.append([val1, self.tail, val2])
    self.tail = len(self.arr) - 1

  def post(self):
    def rec(h, ans):
      l = self.arr[h][1]
      r = self.arr[h][2]

      if type(l) == int:
        ans = rec(l, ans)
      elif type(l) == str:
        ans += l

      if type(r) == int:
        ans = rec(r, ans)
      elif type(r) == str:
        ans += r
        
      ans += self.arr[h][0]
      
      return ans
    ans = rec(self.head, "")
    return ans

tree = Tree(expression[0])
print(tree.head)
isOp = True
isInBracket = 0
op = ''
val = ''
for i in range(1, len(expression)):
  cur = expression[i]
  if isOp:
    if cur == '+' or cur == '-' or cur == '*' or cur == '/':
      op = cur
      isOp = False
    elif cur == '(':
      isInBracket += 1
  else:
    val = cur
    if op == '+' or op == '-':
      if isInBracket > 0:
        tree.addToTail(op, val)
        isInBracket -= 1
      else:
        tree.addToHead(op, val)
    elif op == '*' or op == '/':
      tree.addToTail(op, val)
    isOp = True

print(tree.arr, tree.head)
print(tree.post())