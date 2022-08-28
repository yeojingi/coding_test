from bisect import bisect_left, bisect_right, bisect

N = int(input())
hisCards = list(map(int, input().split(" ")))
M = int(input())
theNumbers = list(map(int, input().split(" ")))

hisCards.sort()

for n in theNumbers:
  print(bisect_right(hisCards, n) - bisect_left(hisCards, n), end=" ")
print()

# arr = list(map(int, "6 3 2 10 10 10 -10 -10 7 3".split(" ")))
# arr.sort()
# print(arr)
# print(bisect_left(arr, 10))
# print(bisect_right(arr, 10))
