'''
1부터 n까지 자연수 중 m개를 고른 수열
같은 수 중복 가능

재귀 활용으로 접근
재귀 함수의 시간복잡도
for 문에서 n번의 안에서 깊이가 m이 될때까지 반복 발생
O(n*m)
'''


def DFS():
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return

    for a in range(1, n + 1):
        ans.append(a)
        DFS()
        ans.pop()
        []


n, m = map(int, input().split())
num = [i for i in range(1, n + 1)]
ans = []
DFS()

