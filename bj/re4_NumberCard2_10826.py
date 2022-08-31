def lowerbound(array, target):
  s, e = 0, len(array)

  while s < e:
    m = (s + e) //2 
    if target <= array[m]:
      e = m
    else:
      s = m + 1
  return s

def upperbound(array, target):
  s, e = 0, len(array)

  while s < e:
    m = (s + e) // 2
    if target < array[m]:
      e = m
    else:
      s = m + 1
  return s - 1

N = int(input())
hisCards = list(map(int, input().split(" ")))
M = int(input())
theNumbers = list(map(int, input().split(" ")))

hisCards.sort()
# print(hisCards)

for n in theNumbers:
  ans = upperbound(hisCards, n) - lowerbound(hisCards, n)
  print((ans+1 if ans >= 0 else 0), end=" ")
print()

