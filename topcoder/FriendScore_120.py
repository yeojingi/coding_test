def solution(s):
  friends = []
  for param in s:
    param = param.replace("N", "0")
    param = param.replace("Y", "1")
    friends.append(param)

  matrix = []
  for friend in friends:
    row = list(map(int, list(friend)))
    matrix.append(row)

  N = len(matrix)
  M = len(matrix[0])

  sum_matrix = [[0] * M for i in range(N)]
  for i in range(N):
    for j in range(M):
      k = 0
      for l in range(M):
        k += matrix[i][l] * matrix[l][j]
      
      if k > 0 :
        sum_matrix[i][j] = 1

  popular = [[0] * M for i in range(N)]
  for i in range(N):
    for j in range(M):
      popular[i][j] = 1 if matrix[i][j] + sum_matrix[i][j] > 0 else 0 
      if i == j:
        popular[i][j] = 0

  for i in range(N):
    popular[i] = sum(popular[i])

  return max(popular)

params = [
  [ "NNN", 
    "NNN",
    "NNN"],
  [ "NYY",
    "YNY",
    "YYN"],
  [ "NYNNN",
    "YNYNN",
    "NYNYN",
    "NNYNY",
    "NNNYN"],
  [ "NNNNYNNNNN",
    "NNNNYNYYNN",
    "NNNYYYNNNN",
    "NNYNNNNNNN",
    "YYYNNNNNNY",
    "NNYNNNNNYN",
    "NYNNNNNYNN",
    "NYNNNNYNNN",
    "NNNNNYNNNN",
    "NNNNYNNNNN"],
]
answers = [
  0,
  2,
  4,
  8
]

for i in range(0, len(params)):
  print(params[i])
  assert solution(params[i]) == answers[i], solution(params[i])

# 왜 이건 풀릴까?
# 이 아이디어는 어떻게 떠올렸을까?
