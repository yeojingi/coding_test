# 220817

def solution(n, east, west, south, north):
  poss = 0
  dy = [0, 0, 1, -1]
  dx = [1, -1, 0, 0]
  d = [east/100, west/100, south/100, north/100]
  tract = []

  def search(n, x, y):
    p = 0
    if n == 0:
      return 1

    tract.append([x, y])
    for i in range(0, 4):
      if d[i] == 0:
        continue

      cx = x + dx[i]
      cy = y + dy[i]
      
      if [cx, cy] not in tract:
        p +=  d[i] * search(n-1, cx, cy)
    tract.pop()
      
    return p
  
  poss = search(n, 0, 0)
  return poss

assert solution(1, 25, 25, 25, 25) == 1.0, solution(1, 25, 25, 25, 25)
assert solution(2, 25, 25, 25, 25) == 0.75, solution(2, 25, 25, 25, 25)
assert solution(7, 50, 0, 0, 50) == 1.0, solution(7, 50, 0, 0, 50)
print(solution(14, 50, 50, 0, 0))
print(solution(14, 25, 25, 25, 25))

# 여러 답이 나오는 연산에서 return 값을 쓰면 항상 이상해져..

# 연습장에서 수학 문제 풀 듯이 다 써서 풀고 나서 옮겨야 한다.
# 약간 수리 논술 풀 듯이 해야하는 것도 있는 것 같네?
# 내가 다 안 다음에 답안지 제출하는 느낌

