[K, N] = list(map(int, input().split(' ')))
Lans = []
for i in range(K):
  Lans.append(int(input()))


l = 0
r = max(Lans)
while True:
  indi = int((l + r) /2)

  temp = 0
  for i in range(K):
    temp += Lans[i] // indi
    print(temp, i)
  
  print(l, r, indi, temp)
  if l >= r:
    break

  if temp == N:
    print(indi)
    break

  if temp > N:
    # 너무 잘게 자름
    # 오른쪽 선택
    l = indi+1
  else :
    r = indi-1

# 3 5
# 100
# 200
# 300
