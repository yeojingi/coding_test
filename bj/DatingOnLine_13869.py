import math

N = int(input())
scores = list(map(int, input().split(' ')))
newScores = [0] * N
scores.sort()
newScores[0] = scores[0]
j = 1
for i in range(1, N):
  if j > 0:
    newScores[j] = scores[i]
    j *= -1
  elif j < 0:
    newScores[j] = scores[i]
    j *= -1
    j += 1
  
area = 0
for i in range(N):
  area += newScores[i] * (newScores[i-1] if i > 0 else newScores[N-1])
area *= math.sin(math.pi * 2 / N) / 2
# area *= math.sin(math.radians(360 / N)) / 2 
# print(round(area, 3))
print('%.3f'%area)