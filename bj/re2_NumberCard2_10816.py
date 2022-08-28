# N = int(input())
# Cards = list(map(int, input().split(' ')))
# M = int(input())
# Numbers = list(map(int, input().split(' ')))

# Cards.sort()

def lowerbound(array, target):
  start, end = 0, len(array)
  while start < end:
    mid = (start+end)//2
    if target <= array[mid]:
      end=mid
    else:
      start=mid+1
  return start

def upperbound(array, target):
  start, end = 0, len(array)
  while start < end:
    mid = (start+end)//2
    if target < array[mid]:
      end=mid
    else:
      start=mid+1
  return start-1

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

# arr = list(map(int, "6 3 2 10 10 10 -10 -10 7 3".split(" ")))
# arr.sort()
# print(arr)
# print(bisect_left(arr, 10))
# print(bisect_right(arr, 10))
