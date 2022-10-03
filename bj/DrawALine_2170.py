N = int(input())
lines = [list(map(int, input().split(' '))) for _ in range(N)]

Ss = [3,5, 7]
Es = [3, 5,7 ]

def upperbound(array, target):
  start, end = 0, len(array)
  while start < end:
    mid = (start+end)//2
    if target < array[mid]:
      end=mid
    else:
      start=mid+1
  return start-1

def lowerbound(array, target):
  start, end = 0, len(array)
  while start < end:
    mid = (start+end) // 2
    if target <= array[mid]:
      end = mid
    else:
      start = mid + 1
  return start

for line in lines:
  u = upperbound(Ss, line[0])
  d = lowerbound(Es, line[1])
  print(u, d)

