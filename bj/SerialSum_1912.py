N = int(input())
arr = list(map(int, input().split(' ')))

dp = [0] * N
dp[0] = arr[0]

for i in range(1, N):
  if arr[i-1]+arr[i] > arr[i]:
    arr[i] += arr[i-1]

print(max(arr))