angles = [int(input()) for _ in range(3)]

if sum(angles) != 180:
  print("Error")
  exit()

# Equilateral
# 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
# 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
isEquilateral = True
for angle in angles:
  if angle != 60:
    isEquilateral = False
    break

if isEquilateral:
  print("Equilateral")
  exit()

isIsosceles = False
for i in range(len(angles)):
  for j in range(i+1, len(angles)):
    if angles[i] == angles[j]:
      isIsosceles = True

if isIsosceles:
  print("Isosceles")
  exit()

print("Scalene")