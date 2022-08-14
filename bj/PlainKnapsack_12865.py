def solution(K, loads):
  m = [0] * (K + 1)

  for load in loads:
    w = load[0]
    v = load[1]
    nm = [0] * (K+1)
    for i in range(1, K+1):
      if i >= w:
        nm[i] = max(m[i], m[i-w] + v)
      else:
        nm[i] = m[i]
    m = nm

  return m[K]

[N, K] = list(map(int, input().split(' ')))
loads = []
for i in range(0, N):
  loads.append( list(map(int, input().split(' '))))

print( solution (K, loads))