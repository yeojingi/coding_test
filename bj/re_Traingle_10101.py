from typing import Set


angles = []
for _ in range(3):
  angles.append(int(input()))

if sum(angles) != 180:
  print("Error")
  exit()

angleSet = set(angles)
if len(angleSet) == 1:
  print("Equilateral")
  exit()
elif len(angleSet) == 2:
  print("Isosceles")
  exit()

print("Scalene")
