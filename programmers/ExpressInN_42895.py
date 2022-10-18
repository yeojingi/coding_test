def solution(N, number):
    dp = [ set([]) for _ in range(9)]
    
    for i in range(1, 9):
        for k in range(1, i):
            l = i - k
            
            for s in dp[k]:
                for a in dp[l]:
                    dp[i].add(s+a)
                    dp[i].add(s-a)
                    dp[i].add(a-s)
                    dp[i].add(s*a)
                    if a != 0:
                        dp[i].add(s//a)
                
        dp[i].add( int(str(N) * (i)) )
        # print(i, dp[i])
        if number in dp[i]:
            return i
        
    # print(dp)
    
    return -1

# print(solution(5, 35))