# 2주차 과제

강의 번호: 알고리즘
유형: 스터디
작성일시: 2022년 7월 16일 오전 2:00

## 재귀함수의 시간복잡도

※참고: https://github.com/2022-DKUS-Summer-Study/Algorithm/issues/15

```python
function f(n):
    if n==0:
        return;
    for i in [1,m]:
        f(n-1)
```

다음과 같은 함수에서 각 재귀 호출별로 함수 f(n)에서  f(n-1)을 호출하는 횟수는 m번이고 이는 총 n번 반복되게 된다.

이때, **T(0)=O(g(n))=O(1), T(n)=O(m)T(n-1)**와 같이 나타낼 수 있고, **T(n)=O(m)O(m)O(m)...O(m)O(1) = O(m^n)**와 같이 계산할 수 있다.

## TSP(외판원 순회 문제)

### 문제

[https://www.acmicpc.net/problem/10971](https://www.acmicpc.net/problem/10971)

외판원 순회 문제는 영어로 Traveling Salesman problem (TSP) 라고 불리는 문제로 computer science 분야에서 가장 중요하게 취급되는 문제 중 하나이다. 여러 가지 변종 문제가 있으나, 여기서는 가장 일반적인 형태의 문제를 살펴보자.

1번부터 N번까지 번호가 매겨져 있는 도시들이 있고, 도시들 사이에는 길이 있다. (길이 없을 수도 있다) 이제 한 외판원이 어느 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 순회 여행 경로를 계획하려고 한다. 단, 한 번 갔던 도시로는 다시 갈 수 없다. (맨 마지막에 여행을 출발했던 도시로 돌아오는 것은 예외) 이런 여행 경로는 여러 가지가 있을 수 있는데, 가장 적은 비용을 들이는 여행 계획을 세우고자 한다.

각 도시간에 이동하는데 드는 비용은 행렬 W[i][j]형태로 주어진다. W[i][j]는 도시 i에서 도시 j로 가기 위한 비용을 나타낸다. 비용은 대칭적이지 않다. 즉, W[i][j] 는 W[j][i]와 다를 수 있다. 모든 도시간의 비용은 양의 정수이다. W[i][i]는 항상 0이다. 경우에 따라서 도시 i에서 도시 j로 갈 수 없는 경우도 있으며 이럴 경우 W[i][j]=0이라고 하자.

N과 비용 행렬이 주어졌을 때, 가장 적은 비용을 들이는 외판원의 순회 여행 경로를 구하는 프로그램을 작성하시오.

### 풀이

- 시간복잡도: O(N^N)

N-Queen문제와 마찬가지로 dfs를 이용한 완전탐색을 이용해 풀었다.

마지막 index에 도달하면 순회 가능한 것으로 판단하여 minimum_cost값과 비교하여 갱신한다.

또한 해당 가지가 유망한지(이전에 방문한 노드인지, 갈 수 있는 도시인지)를 판단하여 유망하지 않으면 더 이상 진행하지 않는다.

## N-Queen

### 문제

[https://www.acmicpc.net/problem/9663](https://www.acmicpc.net/problem/9663)

N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

### 풀이

- 시간복잡도 O(N^N)
![image](https://user-images.githubusercontent.com/74875490/179280329-d5dfcecb-a26e-4e6e-b316-e6e4bde24848.png)
<br>
dfs(깊이 우선 탐색)을 이용한 완전탐색으로 문제를 풀되, 해당 가지가 유망하지 않으면 더 이상 진행하지 않는다.

```python
if promising(idx+1):
            func(idx+1)
```

해당 가지가 유망하면 더 진행

```python
if idx==n:
        cnt=cnt+1
        return
```

마지막 인덱스까지 도달하면 해당말 배치 조합이 유효한것으로 판단하여 cnt+1

<시간초과>

```python
import sys

n=int(sys.stdin.readline())

cnt=0
S=[-1 for i in range(n+1)]
def func(idx):
    global cnt
    if idx==n:
        cnt=cnt+1
        return

    for i in range(1,n+1):
        S[idx+1]=i
        if promising(idx+1):
            func(idx+1)

def promising(idx):
    if idx==1:
        return True
    
    for i in range(1, idx, 1):
        if S[i]==S[idx] or abs(S[i]-S[idx])==abs(i-idx):
            return False
    return True       

func(0)
print(cnt)
```

<통과>

```python
import sys

n=int(sys.stdin.readline())

cnt=0
S=[-1]*(n+1)
def func(idx):
    global cnt
    if idx==n:
        cnt=cnt+1
        return

    for i in range(1,n+1):
        S[idx+1]=i
        if promising(idx+1):
            func(idx+1)

def promising(idx):
    if idx==1:
        return True
    
    for i in range(1, idx, 1):
        if S[i]==S[idx] or abs(S[i]-S[idx])==abs(i-idx):
            return False
    return True       

func(0)
print(cnt)
```

**Q. S=[-1 for i in range(n+1)]을 S=[-1]*(n+1)와 같이 바꾸었을 뿐인데 시간초과에서 통과가 되었습니다. 혹시 이유를 알 수 있을까요?**

## N과 M(3)

### 문제

https://www.acmicpc.net/problem/15651

자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- 1부터 N까지 자연수 중에서 M개를 고른 수열
- 같은 수를 여러 번 골라도 된다.

### 풀이

- 시간복잡도: O(N^M)

깊이가 M인 트리로 생각하여 dfs를 이용한 완전탐색으로 구현

같은 수를 여러 번 골라도 되므로, 해당 가지가 유망한지 여부를 판단할 필요 없이 진행

## 알파 틱택토

### 문제

https://www.acmicpc.net/problem/16571

틱택토(Tic-tac-toe) 게임은 두 플레이어가 번갈아가며 O와 X를 3x3판에 써서 같은 글자를 가로, 세로, 혹은 대각선 상에 놓이도록 하는 게임이다.

먼저 3개의 연속 된 O 또는 X를 완성시킨 플레이어가 승리하게 된다. 이 게임은 무승부가 가능하다.

[https://upload.acmicpc.net/cb7dcaf6-7107-40ee-bf9e-220f1231ca17/-/preview/](https://upload.acmicpc.net/cb7dcaf6-7107-40ee-bf9e-220f1231ca17/-/preview/)

***Figure***: ****게임의 진행과정 예시

틱택토 초보 승현이와 기영이는 틱택토 게임을 플레이하고 있었다. 그런데 뒤에서 지켜보고 있던 틱택토 초고수 윤영이와 진욱이가 너무나 답답한 나머지 본인들이 대신 플레이를 해주겠다고 나섰다.

지금까지 진행 된 틱택토 게임 보드가 주어졌을 때, 이번에 착수하는 플레이어가 얻을 수 있는 최선의 게임 결과는 무엇일까? **단, 두 플레이어는 항상 모든 경우를 고려하여 최선의 수를 둔다고 가정한다.**

### 풀이

행과 열을 모두 고려해야한다는 생각에 어떻게 접근을 할지 고민을 하였습니다.

이중 for문을 통해서 전체 경우의 수를 모두 탐색하는 방법으로 구현하였으나, 아마 최선의 수를 두는 것을 고려하지 못해 계속 오답이 발생하는 것으로 보입니다.

혹시 이 방법을 해결과 관련해서 도움이나 힌트를 받을 수 있을까요?

<오답코드>

```python
import sys
from copy import deepcopy

player={"X":1,"O":2}
board=[]
X_cnt=0
O_cnt=0
for i in range(3):
    board.append([])
    for number in map(int, sys.stdin.readline().rstrip().split()):
        if number==1:
            X_cnt+=1
        elif number==2:
            O_cnt+=1
        board[i].append(number)

result=[]
def play_game(board, player_flag, win_flag):
    ##보드의 모든 곳에 말이 놓여져 있으면 종료, 무승부
    if "W" in result:
        return 

    exit_flag=1
    for i in range(3):
        for j in range(3):
            if board[i][j]==0:
                B=deepcopy(board)
                B[i][j]=player[player_flag]
                if check(B, i, j):
                    if player_flag==win_flag:
                        result.append("W")
                        return
                    else:
                        result.append("L")

                if player_flag=="X":
                    if check_optimal(B, "O")==True:
                        play_game(B, "O", win_flag)
                else:
                    if check_optimal(B, "X")==True:
                        play_game(B, "X", win_flag)
   
    if exit_flag==1:
        result.append("D")
      
def check(B, row, col):
    if B[row][0]==B[row][1]==B[row][2] and B[row][0]!=0:
        return True
    if B[0][col]==B[1][col]==B[2][col] and B[0][col]!=0:
        return True
    if (B[0][0]==B[1][1]==B[2][2] and B[1][1]!=0) or (B[0][2]==B[1][1]==B[2][0] and B[1][1]!=0):
        return True
    return False

def check_optimal(B, target):
    for i in range(3):
        for j in range(3):
            if board[i][j]==0:
                B=deepcopy(board)
                B[i][j]=player[target]
                if check(B, i, j)==True:
                    return False    
    return True

if X_cnt<=O_cnt:
    play_game(board, "X", "X")
else:
    play_game(board, "O", "O")

if "W" in result:
    print("W")
elif "D" in result:
    print("D")
else:
    print("L")
```

