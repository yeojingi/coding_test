# 220813
# if 문을 줄여라

def solution(capacities, bottles, fromId, toId):
  for i in range(0, len(fromId)):
    f = fromId[i]
    t = toId[i]

    sum = bottles[f] + bottles[t]

    bottles[t] = min(capacities[t], sum)
    bottles[f] = sum - bottles[t]

  return bottles

bottles = solution(
  [30, 20, 10],
  [10, 5, 5],
  [0, 1, 2],
  [1, 2, 0]
)

for bottle in bottles:
  print(bottle, end=", ")
  # print("hi", end= "")