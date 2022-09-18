N = int(input())
cards = list(map(int, input().split(' ')))
M = int(input())
ss = list(map(int, input().split(' ')))

def bisect(arr, n):
  def rec(arr, s, e, n):
    if s >= e:
      if s >= len(arr):
        return 0
      elif arr[s] == n:
        return 1
      else:
        return 0

    if arr[s] == n:
      return 1
    
    m = s + (e - s) // 2
    if arr[m] > n:
      return rec(arr, s, m-1, n)
    elif arr[m] < n:
      return rec(arr, m+1, e, n)
    else:
      return 1

  return rec(arr, 0, len(arr), n)

cards.sort()

ans = []
for s in ss:
  ans.append(bisect(cards, s))

print(*ans)