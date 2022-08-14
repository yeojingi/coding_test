def solution(N, prices):
  for i in range(1, N):
    prices[i][0] = min(prices[i-1][1], prices[i-1][2]) + prices[i][0]
    prices[i][1] = min(prices[i-1][0], prices[i-1][2]) + prices[i][1]
    prices[i][2] = min(prices[i-1][0], prices[i-1][1]) + prices[i][2]

  return min(prices[len(prices)-1])

# answer = int(input())
N = int(input())
prices = []
for i in range(0, N):
  s = input()
  arr = map(int, s.split(" "))
  print(arr)
  # arr = s.split(' ')
  prices.append(arr)

print(solution(N, prices))