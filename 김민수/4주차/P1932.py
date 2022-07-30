'''
정수 삼각형
문제에서는 위에서 아래로 내려오면서의 최댓값을 찾으라 하였다.
처음에는 위에서 아래로 내려가는 식으로 찾으려 했지만 이 경우 탐색의 범위가 점점 넓어져서
문제에서 제시한 위에서 아래가 아닌 아래에서 위로 접근하는 방식으로 접근을 하였다.
아래에서 위로 접근하는 방식의 바텀업(상향식) 방법을 사용하며 접근을 하였다.
'''

# 삼각형의 크기
n = int(input())

triangle = [list(map(int, input().rstrip().split())) for _ in range(n)]

for i in range(n - 2, 0, -1):
    for j in range(i):
        if i == 0 or i == j:
            triangle[i][j] += triangle[i + 1][j]
        else:
            triangle[i][j] += max(triangle[i + 1][j - 1], triangle[i + 1][j])

print(triangle)
