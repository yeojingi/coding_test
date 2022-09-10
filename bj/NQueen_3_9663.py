N = int(input())

Qs = [0] * N
ans = 0

def rec(J):
  global ans, Qs
  if J == N:
    ans += 1

  availables = [1] * N

  for j in range(J):
    availables[Qs[j]] = 0

    dia = J - j
    if Qs[j] + dia < N:
      availables[Qs[j] + dia] = 0
    if Qs[j] - dia >= 0:
      availables[Qs[j] - dia] = 0
  
  for i in range(N):
    if availables[i] == 1:
      Qs[J] = i
      rec(J+1)

rec(0)
print(ans)