''' 숫자 입력 리스트'''
n = int(input())
check = sorted(list(map(int, input().split())))

'''숫자 리스트'''
m = int(input())
num = list(map(int, input().split()))


'''
이진 탐색으로는 일단 접근의 방법을 찾지 못함
-> 카운팅 소트 방법을 채용
음수의 인덱스는 존재하지 않으므로 기존의 수에 10000000을 더해서 길이는 똑같은 양수의 숫자배열 입력
check에 있는 숫자를 인덱스로 갖는 배열에 0을 선언, 해당 숫자 등장 시 배열의 값에 1을 더하기
확인하려는 num 리스트의 인덱스를 그대로 호출하여 진행
'''
count = [0 for i in range(0, 20000001)]

for i in check:
    count[i + 10000000] += 1

for i in num :
    print( count[i+10000000], end = " ")