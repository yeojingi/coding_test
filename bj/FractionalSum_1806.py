import math

start = 0
end = 0

N, S = map(int, input().split())
arr = list(map(int, input().split()))
accu = [0] * (N+1)
for i in range(1, N):
  accu[i] += accu[i-1] + arr[i-1]
print(accu)

shortest_length = math.inf
cal = 0

while True:
  cal += 1
  partial_sum = accu[end+1] - accu[start]
  print(cal, start, end, partial_sum)

  if partial_sum > S:
    if end - start < shortest_length:
      shortest_length = end + 1 - start
    start += 1
  else:
    end += 1
  
  if end > N:
    break

print(cal)
print(shortest_length)