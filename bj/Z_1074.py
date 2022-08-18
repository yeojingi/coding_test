[N, I, J] = list(map(int, input().split(' ')))

answer = 0

# I -= 1
# J -= 1
for k in range(0, N):
  i = I % 2
  j = J % 2
  I = int(I / 2)
  J = int(J / 2)

  answer += (2*i + j) * (2**(2*k))

print(answer)

# f'{x:b}' 2진법 표현
# int(str, x) => str을 x승 하며 곱함? 좀 이상한 함수
# => str로 표현된 x진법 수를 decimal로 바꿔주는 함수
# 분할 정복이라는 개념을 배우긴 했다
# 처음엔 맵을 다 그리려고 했음