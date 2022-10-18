T = int(input())
anss = []
for _ in range(T):
  N = int(input())
  s = []
  commands = [ list(input().split(' ')) for _ in range(N) ]
  for command in commands:
    if command[0] == 'I':
      val = int(command[1])
      s.append(val)
      s.sort()

    elif command[0] == 'D':
      if command[1] == '1':
        if len(s) > 0:
          s = s[:-1]
      elif command[1] == '-1':
        if len(s) > 0:
          s = s[1:]
    
  if len(s) > 0:
    anss.append(f"{s[-1]} {s[0]}")
  else:
    anss.append("EMPTY")

print("\n".join(anss))
