from bisect import bisect_right
import sys, math

input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

accum = [0] * (N+1)
for i in range(N):
  accum[i+1] += accum[i] + arr[i]

# print(accum)
minLength = math.inf
for i in range(N):
  if accum[i+1] >= S:
    index = bisect_right(accum, accum[i+1] - S)
    length = i + 1 - index + 1

    # print(i, index, length, minLength, arr[i], accum[i+1], accum[i+1] - S, accum[index])
    if length < minLength:
      minLength = length

if minLength == math.inf:
  print(0)
else:
  print(minLength)