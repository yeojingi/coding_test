# 220817

def solution(relations):
  salaries = [0] * len(relations)

  def recur(n):
    if "Y" not in relations[n]:
      salaries[n] = 1
      return 1

    if salaries[n] != 0:
      return salaries[n]

    for i in range(0, len(relations[n])):
      if relations[n][i] == "Y":
        salaries[n] += recur(i)
    
    return salaries[n]

  for i in range(len(relations)):
    recur(i)

  return sum(salaries)

assert solution(["N"]) == 1, solution(["N"])
assert solution(["NNYN", "NNYN", 'NNNN', 'NYYN']) == 5, solution(["NNYN", "NNYN", 'NNNN', 'NYYN'])
assert solution(["NNNNN", "YNYNNY", "YNNNNY", "NNNNNN", "YNYNNN", "YNNYNN"]) == 17, solution(["NNNNN", "YNYNNY", "YNNNNY", "NNNNNN", "YNYNNN", "YNNYNN"])
assert solution(["NYNNYN", "NNNNNN", "NNNNNN", "NNYNNN", "NNNNNN", "NNNYYN"]) == 8, solution(["NYNNYN", "NNNNNN", "NNNNNN", "NNYNNN", "NNNNNN", "NNNYYN"])
assert solution(["NNNN", "NNNN", "NNNN", "NNNN"]) == 4, solution(["NNNN", "NNNN", "NNNN", "NNNN"])


