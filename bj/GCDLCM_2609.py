[a, b] = list(map(int, input().split(' ')))

def recur(a, b):
  if a % b == 0:
    return b
  
  return recur(b, a%b)


gcd = 0
if a > b:
  gcd = recur(a, b)
else:
  gcd = recur(b, a)

lcm = a * b / gcd

print(gcd)
print(int(lcm))