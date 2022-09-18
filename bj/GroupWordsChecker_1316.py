N = int(input())
words = [input() for _ in range(N)]

ans = 0
for word in words:
  map = {word[0]: 1}
  b = word[0]
  for i in range(len(word)):
    if word[i] == b:
      continue
    else:
      if map.get(word[i]): 
        ans +=1
        break
      else:
        map[word[i]] = 1
        b = word[i]

print(N-ans)