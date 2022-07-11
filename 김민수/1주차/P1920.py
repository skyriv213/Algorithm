import sys

# 입력값 받는 속도 증가
input = sys.stdin.readline

# 문제에서 주어진 예시를 받기위한 부분
# 파이썬에서는 마지막 엔터 부분을 문자로 받기에 따로 rstrip으로 제거
n = int(input())
num = sorted(list(map(int, input().split())))
m = int(input())
check = list(map(int, input().split()))

'''
check 해야하는 리스를 for문을 통해 먼저 하나씩 꺼내오는 방식을 가져왔다.
for문의 반복마다 l,r값을 초기화 해야한다 생각을 하였고 for문 안에 이진탐색의 코드를 넣어 진행을 하였다.
다만 출력문의 경우 어떤식으로 표현을 해야하나 고민을 하다가 boolean타입을 이용해서 False값이면 
0을 출력하는 방식으로 진행을 하였다. 
'''

# 이진탐색을 위한 메서드, 가독성을 조금이라도 올리기 위해 for문안의 메서드를 추출해서 가져왔다.
def binary():
    global ans, l, r
    while l <= r:
        mid = (l + r) // 2
        if num[mid] == i:
            ans = True
            print(1, end = " ")
            break
        elif num[mid] < i:
            l = mid + 1
        else:
            r = mid - 1



# check 리스트를 확인하기 위한 for문
for i in check:
    l, r = 0, n - 1
    ans = False  # 여부확인
    binary()
    if not ans:
        print(0, end = " ")
