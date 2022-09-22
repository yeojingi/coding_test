N = int(input())
arr = list(map(int, input().split(' ')))
arr.sort()

sum = 0
for i in range(N):
  # print(arr[i], i, sum)
  if sum + 1 >= arr[i]:
    sum += arr[i]
  else:
    # print(sum+1)
    break
print(sum+1)