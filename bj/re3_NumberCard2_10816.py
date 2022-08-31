N = int(input())
cs = list(map(int, input().split(' ')))
M = int(input())
ss = list(map(int, input().split(' ')))

cs.sort()
cal = 0

def bs(arr, f):
  global cal
  s = 0
  e = len(arr) -1
  m = (s + e) // 2
  
  while s <= e:
    m = (s + e) // 2
    cal += 1
    # print(arr)
    # print(s, e, m, f)
    if arr[m] < f:
      s = m + 1
    elif arr[m] > f:
      e = m -1
    else:
      break
  if s > e:
    return -1
  else:
    return m

# print(cs)
for s in ss:
  index = bs(cs, s)
  if index == -1:
    print(0, end= " ")
  else:
    end = index
    start = index
    # find upper
    while end+1 < len(cs) and cs[end+1] == s:
      end += 1
    # find lower
    while start-1 >= 0 and cs[start-1] == s:
      start -= 1
    print(end-start+1, end=" ")


# 왜 안 되는지 이해했음
# 아래 upper, lower 찾을 때 N/2 만큼 연산할 수도 있음