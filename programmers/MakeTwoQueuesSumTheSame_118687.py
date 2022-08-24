def solution(queue1, queue2):
  string = queue1 + queue2
  length = len(string)
  goal = int( sum(string) / 2)

  start = 0
  end = len(queue1) -1
  cur = sum(queue1)

  answer = 0
  firstAgain = False

  while cur != goal:
    if start == end:
      return -1
    if cur < goal:
      end = (end + 1) % length
      cur += string[end]
    elif cur > goal:
      cur -= string[start]
      start += 1
      if start == length:
        return -1

    answer += 1

  return answer