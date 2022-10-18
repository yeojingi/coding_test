[K, N] = list(map(int, input().split(' ')))
Lans = []
for i in range(K):
  Lans.append(int(input()))

l = 0
r = max(Lans)
while True:
  indi = int((l + r) /2)


  arr = [0] * K
  temp = 0
  for i in range(K):
    # print(Lans[i] / indi)
    arr[i] =  int(Lans[i] / indi)
    temp += arr[i]

  print(l, r)
  if l >= r:
    break

  if temp > N:
    # 너무 잘게 자름
    # 오른쪽 선택
    l = indi
  else :
    r = indi-1

print(*arr, temp)
print(indi)

# 3 5
# 100
# 200
# 300
