def solution(i):
  K = 0
  for k in range(0, 10000):
    if (k * (k-1) / 2) < i and i <= (k * (k+1) / 2):
      K = k
      break

  I = int(i - (K * (K-1) / 2))
  I = I - 1

  fraction = []
  if K % 2 == 1:
    fraction = [K-I, 1+I]
  else:
    fraction = [1+I, K-I]
  
  fraction = list(map(str, fraction))

  return '/'.join(fraction)

print(solution(int(input())))