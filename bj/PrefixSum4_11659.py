N, M = map(int, input().split())
arr = list(map(int, input().split()))
cumulative = [0] * (N+1)
for i in range(1, N+1):
  cumulative[i] = cumulative[i-1]+arr[i-1]

prefices = [ list(map(int, input().split())) for _ in range(M) ]

for i in range(M):
  [s, e] = prefices[i]
  print(cumulative[e] - cumulative[s-1])