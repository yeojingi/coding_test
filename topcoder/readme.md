## ChessMetrix_247.py

220821  
동적 프로그래밍  
글쎄.. 생각하기 어려울 듯  

지금 내가 생각하는 방법이 완전 탐색보다 나은가? 라는 생각이 들면  
생각을 전개할 자신감이 좀 생길 것 같긴 하다  

## BadNeighbors_235.py

220819  
유한 상태 기계가 굉장히 좋은데??  
점화식을 생각하고,  
이전의 것을 쓸 것에 대해서 생각하면 좋겠다  

나열하듯이 하면 되는데,  
나열할 때 이전의 것을 어떻게 쓸까?  

사실 생각해보니 이게 나열이네? 프로그래밍이라는 게  

### Takeaways
* 유한상태기계로 pseudo coding하는 것 좋다
* 나열 하듯이 생각하면 동적 프로그래밍 쓸 만할 듯?

## CorporationSalary_226.py

220818  
기본적인 동적 프로그래밍  
이 책에서 동적 프로그래밍 정의를 제대로 해준다.  
동적 프로그래밍의 본질은 점화식이 아니라,  
한 번한 계산은 두 번하지 않도록 하는 것.  
결국 하버드에서 말한 Lookup table이라는 것과 일치하는 게 있다  

### Takeaways
* 동적 프로그래밍 = 한 번한 계산은 두 번하지 않는다.

## CrazyBot_148.py

220817  
이미 지나간 자리를 다시 찾게 않도록 하는 방법  
지금 위치를 true로 하고 이어서 DFS/BFS 시킨 다음에 false로 한다.  
이게 DFS/BFS 상관 없이 쓸 수 있는 건가?  
BFS에서는 쓸 수 없을 것 같네.  

보니까 DFS는 하나의 경로 사례를 탐색하고  
BFS는 등위(same-level) 사례를 다루는 구나  
BFS에서는 하나의 사례를 다루는 게 아니기 때문에 tract을 관리해버리면,  
다른 경로 사례의 지나간 흔적에 대한 정보를 다루게 된다.  

### Takeaways
* 이미 지나간 자리를 다시 찾지 않도록 하는 방법 (only for DFS)  
* 그래프로 사고해라.
1. 정점을 고르고
2. edge의 규칙을 찾고, edge를 만들 때 조건 파악하고
3. 다음 node를 파악한다. 
=> 여기서 점화식적인 사고를 유지해야 한다.

## FriendScore_120.py

220816  
이 행렬 연산을 이렇게 풀다니,  
명확하게 만들고 푸는 것이 제일 중요하다  

### Takeaways
* 파이썬의 삼항연산자  
(true value) if (condition) else (false value)  
왜 한번도 못 본 것처럼 생겼지?
* 집합의 조건 수준으로 문제를 분석하자  

## Palindrom_112.py

220816  
문제를 처음에 잘못 풀었다.
홀수 케이스 / 짝수 케이스 다른 줄 모르고 하나를 적용함  

어쩄든 수열 문제 풀듯이
(나열) -> (패턴 파악) -> (일반 규칙 생성) 을 하고, 그 뒤에 코딩을 하는 것일텐데,  
내가 만든 나열, 케이스가 전부를 다 담고 있는지를 생각하지 못한 것 같다.  

그런데 왜 생각하지 못했을까?  

그러게..  

### Takeaways 
* 어떤 기준으로 탐색을 할 지 잘 생각하자

### 의문점
* 나는 왜 전부를 다 담지 못하는 케이스만을 살펴봤을까?