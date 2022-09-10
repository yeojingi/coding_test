angles = [ int(input()) for _ in range(3)]

if sum(angles) != 180:
  print("Error")
  exit()

isEquilateral = True
isScalene = False
for angle in angles:
  if angle != 60:
    isEquilateral = False
if isEquilateral:
  print("Equilateral")
  exit()

if angles[0] == angles[1] or angles[1] == angles[2] or angles[0] == angles[2]:
  print("Isosceles")
else:
  print("Scalene")
