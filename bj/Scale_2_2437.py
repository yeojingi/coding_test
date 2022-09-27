N = int(input())
arr = list(map(int, input().split(' ')))

arr.sort()

s = 0
for i in range(N):
  if s+1 >= arr[i]:
    s += arr[i]
  else:
    break

print(s+1)