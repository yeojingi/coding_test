import math


string = input()
N = len(string)

dp = [ [0] * N for _ in range(N) ]

c = 0
for d in range(N):
  i = N - 1 - d
  for k in range(d+1):
    j = i + k

    if i == j:
      dp[i][j] = 1
      continue
    
    if string[i] == string[j] and (dp[i+1][j-1] == 1 or i + 1 == j):
      dp[i][j] = 1

sdp = [math.inf] * N
sdp[0] = 1

# t= 0
# for j in range(t+1, N):
#   if dp[t][j] == 1:
#     if sdp[j] > sdp[t]:
#       sdp[j] = sdp[t]

# for t in range(N):
#   if t > 0 and sdp[t] > sdp[t-1] + 1:
#     sdp[t] = sdp[t-1] + 1
#     for j in range(t+1, N):
#       if dp[t][j] == 1:
#         if sdp[j] > sdp[t]:
#           sdp[j] = sdp[t]
#   print(sdp)

for j in range(N):
  if j > 0 and sdp[j] > sdp[j-1] + 1:
    sdp[j] = sdp[j-1] + 1
  for i in range(j+1):
    if dp[i][j] == 1:
      if i == 0:
        sdp[j] = sdp[i]
      else:
        if sdp[i-1] + 1 < sdp[j]:
          sdp[j] = sdp[i-1] + 1


print(sdp[-1])