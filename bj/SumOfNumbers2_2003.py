from bisect import bisect_left
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

accum = [0] * (N+1)

for i in range(N):
  accum[i+1] = accum[i] + arr[i]

s = 0
for i in range(1, N+1):
  if accum[i] >= M:
    index = bisect_left(accum, accum[i] - M)
    # print(i, accum[i], index, accum[index], accum[i] >= M)
    if accum[i] - accum[index] == M:
        s += 1

# print(accum)
print(s)