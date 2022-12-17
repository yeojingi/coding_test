import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
boards = [ list(map(int, input().split())) for _ in range(M) ]

anss = []
for board in boards:
  [S, E] = board

  d = E-S
  steps = d // 2

  isPalindrome = True
  for i in range(steps):
    if arr[S - 1 + i ] != arr[E - 1 - i]:
      isPalindrome = False
      break
  
  if isPalindrome:
    anss.append(1)
  else:
    anss.append(0)

for ans in anss:
  print(ans)