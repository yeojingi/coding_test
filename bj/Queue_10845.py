class Queue:
  def __init__(self) -> None:
    self.arr = []

  def front(self):
    return self.arr[0] if len(self.arr) > 0 else -1 

  def back(self):
    return self.arr[-1] if len(self.arr) > 0 else -1

  def empty(self):
    return 0 if len(self.arr) > 0 else 1

  def push(self, item):
    self.arr.append(item)
  
  def pop(self):
    if len(self.arr) == 0:
      return -1
    temp = self.arr[0]

    if len(self.arr) == 1:
      self.arr = []
    else:
      self.arr = self.arr[1:]

    return temp

  def size(self):
    return len(self.arr)

N = int(input())
q = Queue()
# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
comms = [list(input().split(' ')) for _ in range(N)]
ans = []

for comm in comms:
  if comm[0] == 'push':
    q.push(comm[1])
  elif comm[0] == 'pop':
    ans.append(q.pop())
  elif comm[0] == 'size':
    ans.append(q.size())
  elif comm[0] == 'empty':
    ans.append(q.empty())
  elif comm[0] == 'front':
    ans.append(q.front())
  elif comm[0] == 'back':
    ans.append(q.back())

for a in ans:
  print(a)