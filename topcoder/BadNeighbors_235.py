def solution(donations):
  dp = [0] * len(donations)
  N = len(donations)

  k = 2
  dp[0] = donations[0]
  dp[1] = dp[0]
  while k < N-1:
    picked = dp[k-2] + donations[k]
    unpicked = dp[k-1]

    dp[k] = max(picked, unpicked)
    k += 1

  c1 = dp[N-2]

  dp[1] = donations[1]
  dp[0] = 0
  k = 2
  while k < N:
    picked = dp[k-2] + donations[k]
    unpicked = dp[k-1]

    dp[k] = max(picked, unpicked)
    k += 1

  c2 = dp[N-1]

  ans = max(c1, c2)
  print(ans, c1, c2)
  return ans

assert solution([10, 3, 2, 5, 7, 8]) == 19
assert solution([11, 15]) == 15
assert solution([7, 7, 7, 7, 7, 7, 7,]) == 21
assert solution([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 16
assert solution([
  94, 40, 49, 65, 21, 21, 
  106, 80, 92, 81, 679, 4, 
  61, 6, 237, 12, 72, 74,
  29, 95, 265, 35, 47, 1,
  61, 397, 52, 72, 37, 51, 
  1, 81, 45, 435, 7, 36, 
  57, 86, 81, 72]) == 2926