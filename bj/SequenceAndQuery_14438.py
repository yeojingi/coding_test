N = int(input())
As = [0] + list(map(int, input().split(' ')))
M = int(input())
Qs = []
for _ in range(M):
  Qs.append(list(map(int, input().split(' '))))

for query in Qs:
  if query[0] == 1:
    As[query[1]] = query[2]
  elif query[0] == 2:
    # n = query[2] - query[1] + 1
    print(min(As[query[1]:query[2]+1]))
    
