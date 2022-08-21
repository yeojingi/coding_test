N = int(input())
arr = list(map(int, input().split(' ')))

d = dict()
for a in arr:
  d[a] = 1

b = []
for key in d.keys():
  b.append(key)

b.sort()

o = 0
for l in b:
  d[l] = o
  o += 1

c = []
for i in range(0, N):
  c.append(str(d[arr[i]]))

print(" ".join(c))

# bisect 라는 게 있네
# sorted 쓰면 배열된 것을 바로 반환하는 구만 (원본은 안 건드림) sort는 리턴 값이 None
# * 라는 연산자가 컨테이너 타입의 데이터를 언패킹하는 데에 쓰일 수 있다
# N + N + NlogN + N의 연산
# 뭐 크게 문제는 없을 것 같네