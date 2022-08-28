arr = list(map(int, list(input())))

start = arr[0]
same = True
ans = 0
for o in arr:
  if o == start and same == False:
    same = True
  elif o != start and same == True:
    ans += 1
    same = False

print(ans)