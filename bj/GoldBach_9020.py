i = 0
primeNumbers = [ _ for _ in range(2, 10001)]
while i < len(primeNumbers):
  n = primeNumbers[i]
  k = i + 1
  while k < len(primeNumbers):
    if primeNumbers[k] % n == 0:
      primeNumbers.pop(k)
    else:
      k += 1
  i += 1

T = int(input())
anss = []
for _ in range(T):
  N = int(input())
  for i in range(N//2 , N):
    j = N - i
    if i in primeNumbers and j in primeNumbers:
      anss.append(f"{j} {i}")
      break

print(*anss, sep="\n")