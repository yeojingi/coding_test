N = int(input())
SGs = list(map(int, input().split(' ')))
M = int(input())
Cards = list(map(int, input().split(' ')))

M = {}
for SG in SGs:
  if M.get(SG):
    M[SG] += 1
  else:
    M[SG] = 1
  
ans = ""
for Card in Cards:
  d = ""
  if M.get(Card):
    ans += str(M[Card]) + " "
  else :
    ans += '0 '
print(ans)