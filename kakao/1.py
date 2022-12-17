import math
import sys
sys.setrecursionlimit(10**6)

def solution(numbers):
    answer = []
    ss = []
    for number in numbers:
        s = bin(number)[2:]
        k = len(s)
        n = math.ceil( math.log(k + 1) / math.log(2))
        
        s = "0" * (2 ** n - 1 - k) + s
        ss.append(s)

    for string in ss:
        cs = gen(0, len(string), list(string), ['0'] * len(string))
        print(cs)
    

    return answer

def gen(s, e, string, genS):
    if s == e:
        genS[s] = string[s]
        return genS
    m = (s + e) // 2
    
    if string[m] == 0:
        return genS
    else:
        genS[m] = 1
        genS = gen(s, m-1, string, genS)
        genS = gen(m+1, e, string, genS)

    return genS

print(solution([7, 5]))

