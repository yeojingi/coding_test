N = int(input())
Cards = list(map(int, input().split(' ')))
M = int(input())
Numbers = list(map(int, input().split(' ')))

Cards.sort()

for number in Numbers:
  s = 0
  e = len(Cards)-1
  start = 0
  while s <= e:
    m = int((s + e) / 2)

    if Cards[m] < number:
      while Cards[m] < number and m < N-1:
        m = m + 1
      s = m + 1
    elif Cards[m] > number:
      while Cards[m] > number and m > 0:
        m = m - 1
      e = m - 1
    else:
      start = m
      break
  
  if s > e:
    print(0, end=" ")
  else:
    end = start
    while start > 0:
      if Cards[start-1] == number:
        start -= 1
      else:
        break
    while end < len(Cards)-1:
      if Cards[end+1] == number:
        end += 1
      else:
        break
    print(end-start+1, end=" ")
print()
