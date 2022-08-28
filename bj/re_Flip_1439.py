arr = list(map(int, list(input())))

d = arr[0]
i = 0
ans = 0
while i < len(arr):
  if arr[i] != d:
    ans += 1
    while i < len(arr) and arr[i] != d :
      i += 1
  i+=1

print(ans)