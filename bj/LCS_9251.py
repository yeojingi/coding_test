str1 = input()
str2 = input()
I = len(str1)
J = len(str2)

dp = [ [0] * (J+1) for _ in range((I+1))]

# for i in range(I):
#   c = str1[i]
#   for j in range(J):
#     if dp[i+1][j] != dp[i][j+1]:
#       dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
#     elif str2[j] == c:
#       dp[i+1][j+1] = dp[i][j+1] + 1
#     else:
#       dp[i+1][j+1] = dp[i][j+1]

for i in range(I):
  c = str1[i]
  for j in range(J):
    if c == str2[j]:
      dp[i+1][j+1] = dp[i][j] + 1
    else :
      dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
    # elif str2[j] == c:
    #   dp[i+1][j+1] = dp[i][j+1] + 1
    # else:
    #   dp[i+1][j+1] = dp[i][j+1]
      
# for d in dp:
#   print(d)
print(dp[I][J])
