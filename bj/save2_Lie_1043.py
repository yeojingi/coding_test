def solution(N, Ts, Ps):
  STs = set(Ts)
  v = [1] * len(Ps)
  NSTs = set(STs)

  tV = Ts

  # 이럴 땐 자연어로 표현해라.
  # 일단 진실을 알고 있는 사람을 탐색 대상으로 한다
  # 파티를 돌아다니며 진실을 알고 있는 사람이 있는지 확인한다
  # 진실을 알고 있는 사람이 있다면,
  #   (무언가)
  #   그리고 그 파티를 지운다

  # 잘 안될 때는 완전 탐색
  # 그래프 탐색에 대해 자신이 없어서 이러는 것 같아
  # 그래프에 대해서 복습하고 풀자

  while len(tV) > 0:
    T = tV[0]
    tV = tV[1:]

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
  if aP[0] == 0:
    aP = []
  else:
    aP = aP[1:]
  Ps.append(aP)

print(solution(N, Ts, Ps))

# linked list랑 matrix 쓸 때 복습하자 (포프)

# 5 4
# 0
# 2 1 2
# 1 3
# 3 2 3 4
# 0 

# 5 1 
# 0
# 0 
# 0