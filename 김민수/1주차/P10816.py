# '''
# 이진 탐색으로는 일단 접근의 방법을 찾지 못함
# -> 카운팅 소트 방법을 채용
# 음수의 인덱스는 존재하지 않으므로 기존의 수에 10000000을 더해서 길이는 똑같은 양수의 숫자배열 입력
# check에 있는 숫자를 인덱스로 갖는 배열에 0을 선언, 해당 숫자 등장 시 배열의 값에 1을 더하기
# 확인하려는 num 리스트의 인덱스를 그대로 호출하여 진행
# '''
# count = [0 for i in range(0, 20000001)]
#
# for i in check:
#     count[i + 10000000] += 1
#
# for i in num :
#     print( count[i+10000000], end = " ")

def binary_search(s, e):
    global result
    while s <= e:
        mid = (s + e) // 2
        if check[mid] == i:
            result = dic[i]
        if check[mid] < i:
            s = mid + 1
        else:
            e = mid - 1


import sys

input = sys.stdin.readline
''' 숫자 입력 리스트'''
n = int(input())

check = sorted(list(map(int, input().split())))
'''숫자 리스트'''
m = int(input())

num = list(map(int, input().split()))

'''
계속 고민을 하였지만 따로 중복이 되는 부분을 처리하는 방법은 찾지 못하였다. 
그래서 딕셔너리를 채택을 하였고 딕셔너리 채택을 통해 해당 중복 값이 존재 시 value를 증가시켰다.
값을 출력하는 경우 처음 출력을 해야하는 result를 0으로 선언
만약 값이 딕셔너리의 키가 된다면 그 값을 result에 넣어주는 방식을 가져왔다. 
'''
dic = {}
for i in check:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

for i in num:
    s, e = 0, n - 1
    result = 0
    binary_search(s, e)
    print(result, end = " ")

