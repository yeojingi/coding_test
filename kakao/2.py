def solution(n, m, x, y, r, c, k):
    answer = ''

    horizontal = abs(c - y)
    vertical = abs(x - r)

    if abs(k - horizontal - vertical) % 2 != 0:
        answer = 'impossible'
        return answer
    if abs(horizontal + vertical) > k:
        answer = 'impossible'
        return answer
    
    l = len(answer)
    d = abs(c - y) + abs(x - r)
    while d < k - l:
        # print(d, k, l, x, y, answer)
        # ud
        if x+1 <= n:
            answer += 'd'
            x += 1
        elif y-1 > 0:
            answer += 'l'
            y -= 1
        elif y+1 <= m:
            answer += 'r'
            y += 1
        # ud
        elif x-1 > 0 :
            answer += 'u'
            x -= 1
        # lr
        # rl
        
        d = abs(c - y) + abs(x - r)
        l += 1

    # d
    while x < r:
        x += 1
        answer += 'd'

    # l
    while y > c:
        y -= 1
        answer += 'l'
    
    while y < c:
        y += 1
        answer += 'r'
    
    while x > r:
        x -= 1
        answer += 'u'
    
    return answer