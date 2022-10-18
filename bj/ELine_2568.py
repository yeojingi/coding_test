from copy import copy, deepcopy


N = int(input())
lines = [list(map(int, input().split(' '))) for _ in range(N)]

def order(arr, k):
  dict = { arr[i][k]: i  for i in range(len(arr))}
  newArr = copy(arr)

  newArr.sort(key= lambda x: x[k])
  for i in range(len(newArr)):
    arr[dict[newArr[i][k]]][k] = i

print(lines)
order(lines, 0)
print(lines)
order(lines, 1)
print(lines)