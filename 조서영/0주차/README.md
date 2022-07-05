# 0주차 과제

강의 번호: 알고리즘
유형: 스터디
작성일시: 2022년 7월 2일 오전 12:43

1. 7주간 과제를 하며 사용할 언어를 고르고 그 언어에서 제공하는 자료 구조들을 조사
2. 삽입, 삭제, 탐색에 대한 시간 복잡도와 사용법, 그리고 어떤 자료구조를 구현한 것인지에 대해 정리ex)python의 deque, list, set, dictionary

---

# **list**

1. list는 임의의 위치에 있는 원소에 접근이 가능하다. 따라서 스택 자료구조라고 볼 수는 없다.
2. 시간복잡도

| 삽입(append) | O(1) |
| --- | --- |
| 삭제(pop): 마지막 원소 | O(1) |
| pop(0): 첫번째 원소  | O(N) |
| 탐색 | O(N) |
| reverse() | O(N) |
| sort() | O(nlgn) |

# **deque**

1. 자료구조: 큐, 덱
2. 시간복잡도

| right end 삽입(append) | O(1) |
| --- | --- |
| left end 삽입(appendeft) | O(1) |
| right end 삭제(pop) | O(1) |
| left end 삭제(popleft) | O(1) |

→파이썬의 Deque는 내부적으로 **double-linked list**로 구현되어 있다.

→파이썬에는 Queue도 있고, Deque도 있다. Queue는 멀티스레딩도 지원하는 라이브러리여서 Deque보다 느리다. 알고리즘 문제를 푸는 입장이므로 Deque를 사용하는 것이다.

# **set**

1. 자료구조: 집합
2. 시간복잡도

| 삽입(Add) | O(1) |
| --- | --- |
| 삭제(Remove): 해당 원소가 없어도 정상진행 | O(1) |
| 삭제(Discard): 해당 원소가 존재하지 않으면 error발생 | O(1) |
| 합집합(Union) | O(len(s)+len(t)) |
| 교집합(Intersection) | O(len(s)+len(t)) |
| 차집합(Difference) | O(len(s)+len(t)) |
| 대칭차집합(Symmetric Difference) | O(len(s)+len(t)) |
| 탐색(집합의 모든 element들을 순회) | O(N) |

→**중복을 제거**하는 것이 큰 특징이다.

# **dictionary**

1. 자료구조: Map
2. 시간복잡도

| 삽입(D[k]=v) | O(1) |
| --- | --- |
| 삭제(D.pop(k)) | O(1) |
| 탐색(집합의 모든 element들을 순회) | O(N) |

→추가로, c++같은 경우는 O(logN)이 되는데 이는 c++의 맵은 속을 들여다 보면 이진 그래프로 구현이 되어있기 때문이고, **python의 딕셔너리의 경우는 해시로 구현**이 되어있기 때문이다.

# **Heapq**

1. 자료구조: 우선순위큐
2. 시간복잡도

| heap에 item을 넣은 후 배열 수정(heappush(heap, item)) | O(lgN) |
| --- | --- |
| 최소값 출력 후 배열 수정(heappop(heap)) | O(lgN) |
| list x를 heap구조로 변환: heapify(x) | O(NlgN) |

→파이썬은 **MinHeap**이다.(최솟값이 트리의 최상단에 위치하는 형태)

→힙 요소는 tuple일 수 있다.

```python
>>> h=[]
>>> heappush(h, (1, 'a'))
>>> heappush(h, (2, 'b'))
>>> heappop(h)
(1, 'a')
```

# Anytree

1. 자료구조: 트리
2. 시간복잡도

| 삽입 | O(lgN) |
| --- | --- |
| 삭제 | O(lgN) |
| 탐색 | O(lgN) |

```python
>>> !pip install anytree
>>> from anytree import Node, RenderTree
>>> root=Node(10)
>>> level1_child1=Node(34, parent=root)
>>> level1_child2=Node(89, parent=root)
>>> level2_child1=Node(45, parent=level1_child1)
>>> level2_child2=Node(50, parent=level1_child1)
>>> # Tree Structure
>>> #        10
>>> #       /  \
>>> #      34   89
>>> #     /  \
>>> #    45  50 
```

하지만 본인은 dictionary를 이용한 트리구현 방법을 더 많이 사용한다.

```python
N=int(sys.stdin.readline())
G={}
##1. 그래프 초기화
for _ in range(N-1):
    a,b=map(int, sys.stdin.readline().split())
    if a not in G:
        G[a]=[]
    if b not in G[a]:
        G[a].append(b)
    
    if b not in G:
        G[b]=[]
    if b not in G[b]:
        G[b].append(a)
```