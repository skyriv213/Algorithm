'''
가장 긴 증가하는 부분수열
이번에는 메모이제이션 기법을 이용해서 기존 수열과의 길이 비교에 사용된다.
메모이제이션을 사용하는 동적계획법의 이번 문제의 시간복잡도는 for문의 반복
첫번째 반복문에서 n번 그 다음 반복문은 i까지 반복을 하는데 마지막에서 n번만큼 반복하기에
시간복잡도는 o(n^2)이라고 생각한다.


'''

n = int(input())
num = list(map(int, input().split()))
memo = [0 for i in range(n)]

for i in range(n):
    for j in range(i):
        if num[i] > num[j] and memo[i] < memo[j]:
            memo[i] = memo[j]
    memo[i] += 1

print(max(memo))
