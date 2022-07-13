# Algorithm
2022_Summer_Algorithm_Study_Repo

### 시작의 이유

기존에 자바랑 웹 개발의 백엔드 쪽에 흥미를 가지고 공부를 해서 기존에는 자바를 이용하여 코딩 테스트 준비를 하였다.

하지만 자바를 이용한 문제풀이에 어느정도 한계점을 느끼게 되었고 그 대안책으로 파이썬을 생각하게 되었다. 자바도 내가 그 안에 구현이 된 훌륭한 기능을 제대로 사용하지 못하는 것이지 휼룡한 언어라 생각을 한다. 다만 알고리즘 문제풀이에는 짧은 식견으로나마 파이썬이 조금 더 적합하다고 생각을 하여 파이썬을 코딩 테스트 풀이 언어로 선택하게 되었다.

파이썬의 경우 다른 언어보다 좀 더 알고리즘 문제 풀이에 대한 라이브러리가 존재한다. 이는 강력한 장점이다. 내가 사용하고자 하는 메서드가 이미 라이브러리 안에 구현이 되어있다면 그냥 가져다가 쓰면 되는 것이다. 혹여 다른 언어를 사용했으면 직접 구현해야하는 과정을 생략하는 것이기에 시간 다툼을 해야 하는 코딩 테스트에 강력한 장점이라 생각을 하여 파이썬을 고르게 되었다.

### 시간 복잡도

문제를 해결하는데 걸리는 시간, 입력의 함수 관계를 의미한다. 주로 빅-오(Big-O) 표기법을 사용한다.


n의 크기에 따라 각각의 속도는 확연하게 차이가 나기에 시간 복잡도에 맞춰서 문제풀이에 관한 자료구조를 사용해야 한다.  

O( 1 ) < O( log n ) < O( sqrt (N) ) < O( n ) < O( n(log(n)^k) ) < O( n^k ) < O( a^n ) < O( n! ) < O ( n^n )??

### 자료구조 & 라이브러리

문제풀이를 위해 공부하게 된 언어인 만큼 해당 언어에서 제공하는 자료구조와 라이브러리를 잘 알고 있어야 한다고 생각한다. 비록 처음부터 모든 자료구조와 라이브러리를 꿰고 시작할 수는 없겠지만 가장 기본적인 자료구조와 라이브러리를 살펴보고 넘어보고 넘어가 보자.?

### 자료구조

파이썬에서는 기본적으로 많은 자료구조를 제공한다. 각 자료구조에 대해 간략하게 정리를 해보고자 한다. 해당 자료구조의 특징이랑 각각 언제의 상황에서 사용이 되는지, 또한 각 자료구조의 시간 복잡도는 어떻게 되는지 간략하게 정리하고자 한다.?

| 자료구조 | 특징 |  |  | 시간복잡도 |
| --- | --- | --- | --- | --- |
| 리스트 | 순서 및 index에 맞춰서 접근 가능 |  |  | append - O(1)   remove - O(n) |
| 집합 | 인덱스 x, 중복 원소 x |  |  | 특정 원소 유무 확인 - O(1) |
| 딕셔너리? | key : value 구조로 이루어진 데이터는 리스트보다 빠른 처리? |  |  | 데이터 검색 및 수정 - O(1) |
| 큐 | 선입선출 |  |  | insertion - O(1)   deletion -? O(1)   search - O(n) |
| 스택 | 선입후출 |  |  | insertion - O(1)   deletion -? O(1)   search - O(n) |
| 트리 | 비선형   원소 탐색에 사용 |  |  | search - O(log n)   \* 편향적으로 치우쳐진 트리의 경우   \-O(n) |
| 덱 | 앞, 뒤로 삽입 및 삭제 가능   큐와 스택의 장점의 합 |  |  | insertion - O(1)   deletion / pop -? O(1)   remove - O(n)   search - O(n) |
| 우선순위 큐 | 완전 이진트리 형태의 힙을 이용해 구현 |  |  | 삽입 - O(log n)   삭제 - O(log n)   정렬 - O(n log n) |

많은 자료구조들이 존재를 하며 각각의 문제에 맞춰 해당 자료구조를 적용할 수 있는 것이 문제 풀이의 첫 번째 단계라 생각한다.

### 주요 라이브러리

파이썬을 택하게 된 가장 큰 이유인 라이브러리이다. [https://www.acmicpc.net/](https://www.acmicpc.net/)

?[Baekjoon Online Judge

Baekjoon Online Judge 프로그래밍 문제를 풀고 온라인으로 채점받을 수 있는 곳입니다.

www.acmicpc.net](https://www.acmicpc.net/)

백준에 있는 문제들은 알고리즘 관련 문제들을 제시하고 있다. 이와 관련된 문제를 풀 때 유용하게 쓰는 라이브러리를 정리해보고자 한다. 기본 함수 / itertools / heapq / bisect / collections / math가 존재하며 이 중에서 종종 등장하는 함수들을 정리하고자 한다.

|    기본함수 ( import sys )       |  |
| --- | --- |
| 입/출력 |    input() / print()       |
|    sys.stdin.readline().rstrip()       |
| 속도 :? readline() >? input()? |  |
| 데이테 계산 / 정렬   arr = \['a','b','c'\]   n = int형 데이터 타입 |    sum() - iterable 객체의 모든 원소의 합 반환       |
|    max / min() - 최대/최소 값 반환       |
|    eval() - 수학 수식이 문자열 형태로 입력 시   해당 수식 계산 값 반환       |
|    sorted() - 정렬된 결과값 반환      \-key를 이용하여 정렬기준 명시 가능   reverse 속성 이용시 리스트 뒤집기 가능      Ex) sorted(arr, reverse = True) -> 내림차순 정렬       |
|    enumerate      \- 순서가 있는 자료형을 받아서 인덱스 값을 포함하는 객체를 반환      for i? sc in enumerate( arr ) :   print( i , sc )       |
| [아스키코드](https://skyriv312079.tistory.com/23)? |    chr / ord()   \- 아스키 코드로 변환    |
|    itertools ( from itertools import permutations , combinations, product, combinations\_with\_replacement )       |  |
| 순열 / 조합   arr = \['a','b','c'\]   n = int형 데이터 타입 |    permutations(arr, n)   \- iterable 객체에서 n개의 데이터 순열?   순서 고려       |
|    combinations(arr, n)   \- iterable 객체에서 n개의 데이터 조합   순서 고려 x       |
|    product(arr, n)   \- iterable 객체에서 n개의 데이터 조합   중복을 허용한 순열 계산       |
|    combinations\_with\_replacement(arr, n)   \- iterable 객체에서 n개의 데이터 순서를 고려하지않고 나열   중복 조합       |
|    bisect ( from bisect import bisect\_left , bisect\_right )       |  |
| 이진탐색   \- 정렬된 데이터에서 사용 가능   arr = \[1, 2, 3, 4, 6\]   n = int형 데이터 타입 |    bisect\_left(arr, n)   \- 왼쪽을 기준으로 데이터 n이 삽입될 인덱스 찾기      bisect\_right(arr, n)   \- 오른쪽을 기준으로 데이터 n이 삽입될 인덱스 찾기      시간복잡도 o(logN)          |
| collection ( from collections import deque , Counter)    |  |
| 자료구조      arr = \[1, 2, 3, 4, 6\]       | deque      \- 큐를 구현 시 사용, 스택으로도 사용가능   \- 맨 앞/뒤를 동시에 접근 가능하다는 장점   \- popleft () : 맨 앞 원소 제거 / pop () : 맨 뒤 원소 제거   \- appendleft ( n ) : 맨 앞 원소 삽입?   \- append ( n ) : 맨 뒤 원소 삽입??? |
| counter      \- 등장횟수를 세는 기능 제공   \- 원소 별 등장 횟수를 세는 기능이 필요할 때 구현 가능   ?   counter = Counter(arr)? |
|    math ( import math )       |  |
| 수학적 기능 | factorial(n)?   \- n ! |
| sqrt ( n )?   \- n 의 제곱근 |
| gcd( a , b )   \- a, b의 최대 공약수? |
| pi?   \- 상수 파이(pi) |
| e   \- 자연상수 e |