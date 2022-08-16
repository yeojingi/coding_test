def solution(N, Ts, Ps):
  STs = set(Ts)
  v = [1] * len(Ps)
  NSTs = set(STs)

  for T in STs:
    for P in Ps:
      if T in P:
        NSTs.update(P)
  
  v = [1] * len(Ps)
  for T in NSTs:
    for i in range(0, len(Ps)):
      if T in Ps[i]:
        v[i] = 0

  print(f"NSTs: {NSTs}")
  print(f"Ps: {Ps}")
  print(f"v: {v}")

  return sum(v)

[N, P] = list(map(int, input().split(' ')))
T = list(map(int, input().split(' ')))
I = T[0]
Ts = T[1:]

Ps = []
for i in range(0, P):
  aP = list(map(int, input().split(' ')))
  aP = aP[1:]
  Ps.append(aP)

print(solution(N, Ts, Ps))

# set 함수, set의 update 함수
# 지금 이 코드 저장하고, 다시 풀어보자
# 문제가 뭔지 모르겠는데 엄청 안 풀리는 중
# 이건 한 단계 전파만 된다고 생각했다
# 근데 연결된 애들은 다 제거해야 한다. 그래서 그래프 문제구만!