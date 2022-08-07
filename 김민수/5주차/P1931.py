'''
정렬의 경우 기본적으로 오름차순을 기준으로 정렬이 된다
끝나는 시간 기준으로 정렬을 우선적으로 하며 그 뒤 그 안에서 시작하는 시간을 기준으로 정렬을 한번 더 한다
한 회의실에서 가능한 최대 회의 수를 구하는 문제이므로 저장이 된 tmp가 i보다 작은 경우 회의의 수를 늘려주면 된다.

시간 복잡도는 파이썬에서 제공하는 sort함수의 O(n log n)이라 생각을 하며 추후에 o(n)번만큼
반복문이 존재하지만 앞에서 한 sort의 시간복잡도가 더 크기에 시간복잡도는 o(n log n)이라 생각한다.
'''

n = int(input())
room = []

for i in range(n):
    s, e = map(int, input().split())
    room.append([s, e])

room = sorted(room, key = lambda x: (x[1],x[0]))

cnt = 0
tmp = 0

for i, j in room:
    if i >= tmp:
        cnt += 1
        tmp = j

print(cnt)
