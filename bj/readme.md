# 문제풀이, 학습 노트

## Lie_1043.py

220816  
어제 풀다가 못 풀어서 뒀다가 다시 품  
처음에는 (진실을 아는 사람) | (진실을 아는 사람과 파티를 같이 해본 사람)만 피하면 되는 줄 알았는데,  
알고보니 (진실을 아는 사람)에 접근할 수 있는 모든 사람과 파티를 참석하면 안되는 것이었다.  

일차적인 문제는 __문제를 잘못 이해했다__ 는 점이다.  

그래프 문제라는 것을 알게 되었을 때, 내가 그래프에 대해서 자세히 알고 있지 않다는 느낌이 들면 더 풀기가 힘들어진다.  
자신감이 깎여서 그러는 듯  
기본적인 모든 자료구조에 대해서 알고 있다는 자신감이 필요하다.  
이것은 토스 코딩 테스트를 볼 때도 느꼈던 점이다.  

분명히 명심해야 할 것은, 말로 잘 나오지 않는데 코드로는 잘 나올 수 없다는 것이다.  
말로 잘 안나오는데 코드를 짜다보면 말이 나오게 되는 일도 없는 것 같다.  
문제를 정확히 이해하고, 풀이 또한 잘 설명할 수 있는 수준까지 자연어로 계속 사고해야 한다.  

### Takeaways
* set을 쓰면 된다. set을 만들 때 parameter로 배열을 넣을 수 있다
* set에 update를 하면 배열 단위로 set에 요소 추가를 할 수 있다
* 말로 풀어쓸 수 있는 수준이 되어야 한다.

## FindDivison_1193.py

220814  
풀다 만 문제 하나 처리한 거.  
옛날에 풀다 말았다. 알고리즘 푼 지 얼마 안 돼서 이 정도의 구현 문제도 부담이 돼서 풀다 말았었다.  

접근 방법은, 대각선 row를 담당하는 a_k 수열을 생각하고, 그 수열 내부의 순서를 담당하는 b_k라는 수열을 생각했다.  

a_k에 해당하는 k를 구하기 위해 등차수열 합을 이용했는데, 너무 수능 수열 문제 푸는 것 같아서 거부감이 들었다.  
그럼에도, 수열 방법을 썼음에도 구현에서는 프로그래밍 능력이 필요했다.  
__수능 문제 풀 듯이 접근하는 것에 거부감을 가지지 않아도 될 것 같다__  

그리고 a_k를 알게 된 뒤, b_k를 구할 때 나머지를 썼는데 그게 경계에서 문제를 일으켰다.  
다시 살펴보니, 나머지로 접근할 게 아니라 뺴기로 접근할 개념이었다.  
중간에서는 같은 행동을 하지만 경계에서는 다른 행동을 한다  
같은 behavior 를 하더라도, 문제 풀이의 개념과는 다른 implementation을 하고 있을 수 있다.  

더하기를 그냥 k * (k+1) / 2 를 쓰고 있는데, 이게 길다 보니 실수의 여지가 있었고,  
디버깅을 할 때 여기서 실수가 없었는지도 체크했어야 했다.  
```
def sum(k):  
  return k * (k+1) /2  
```
를 만들어서 모듈화 했으면 더 좋았을 것 같다  

### Takeaways
* test case 만들 때 경계 체크가 중요한 것 같다.
* 긴 수식은 함수화해서 디버깅하기 편하게 하면 좋겠다
* str에다가 join(배열)을 한다. 좀 이상하게 생겼는데,,
* 수능 수열적으로 접근해도 괜찮다. 그래도 복잡한 프로그래밍은 남아있다. 꼼수라고 생각하지 말자.

### 의문점

## PlainKnapsack_12865.py

220814  
동적 계획법 공부  

역시 점화식 개념처럼 접근 했다.  
잘 떠오르지 않아서 생각을 좀 했다.  

처음에 동적 계획법을 적용하려고 했을 때 들었던 고민이 있는데,  
메모이제이션 배열 m이 있고, 이번 단계에서 (w)eight, (v)alue인 짐을 넣으려고 하는데,  
m[i-w] 을 그대로 적용해도 되는 걸까?  
같은 m[i-w]이더라도 무게가 얼마나 남았는지에 따라 다르게 취급해야 하는 것 아닌지에 대한 의문이 들었다.  
그런데 이것은 m[i-w-??]이란 배열에 이미 반영이 되어 있는 정보였다.  
__의문을 명확하게 하는 것이 좋은 것 같다.__  

그럼에도 불구하고 한번 실패를 했는데 그 이유는 메모이제이션 배열을, 이전 단계의 배열을 안 쓰고 지금 단계의 배열을 썼다.  
만약에 무게가 1이고 가치가 10인 애가 있다면,  
[10, 20, 30, 40, ...] 계속해서 늘어난다.  
언어로 명확하게 하지 않은 부분에서부터 이런 실수가 다시 나타나는 것 같다.

### Takeaways
* 알고리즘을 짤 때 드는 의문을 언어로 명확히 하자  
* 그리고 실력이 는다는 것은 하나의 인간 언어 문장으로 나온 생각이 쉽게 다뤄지는 것 같다.  
그러니까, 메모이제이션 배열을 만들자라는 생각이 들 때, 이전 배열을 써야한다는 것까지 자연스럽게 다뤄지지 않으니까 실수가 발생한다.  
결국 linking&chunking을 통해 숙련되는 것이 알고리즘에도 적용되는 것이다.  
* 예제로 자주 나오는 것인데 혼자서 풀어보려고 하니까 막히는 부분이 있긴 하다.

### 의문점
* (없음)


## RGBDistance_1149.py

220813  
동적 계획법 공부하려고 풀었다.

하버드에 나온 유튜브 [링크](https://www.youtube.com/watch?v=0y5UkZc-C8Y&t=1049s) 에서 동적계획법은 룩업테이블 알고리즘이라고 해서 동적 계획법 풀 때 룩업테이블을 만드려고 노력했는데 그게 아닌 것 같다.  
수학적 귀납법/ 점화식으로 접근하는 게 더 맞는 듯.  
이 문제는 점화식 적으로 접근했다.  
잘 풀린 듯.  
완전 탐색으로 풀려고 하다가 동적계획법적 방법을 찾았다.  
동적 계획법은 처음 풀 때 동적계획법으로 풀어야겠다는 계획이 잘 나오지 않는다고 POCU 강의에서 그랬는데, 이번에 문제 풀 때 딱 그랬다.

### 파이썬 팁
* arr = list(map(int, s.split(" ")))  
 -> 문자열을 숫자 배열로 만들 때 쓸 수 있다.  
 -> int라는 함수를 s.split(" ")라는 iterable에 적용한 다음에 이것을 list화 해준 것이다.  
 -> return 결과가 map object 여서 배열처럼 쓰려면 list를 해줘야 하는 것이다  
 
 ### Takeaways
 * map 함수 => 꼭 여기서가 아니더라도, 배열에 따라 뭔가 함수를 적용해야할 때 쓸 수 있겠다.  
 자바스크립트로 치면 map, forEach를 통한 컴퓨팅에 썼던 사고가 필요할 때 저 함수를 쓰면 될 듯  

### 의문점
* 완전 탐색보다 검색량이 줄어든 지는 모르겠다.  