'''
한변의 크기가 2^N인 정사각형 배열
r행 c열을 몇번째로 방문하는지 답 도출
배열이지만 정해진 규칙을 가진 문제이므로 공간복잡도를 위해 배열의 선언은 하지않는다.
진행의 방식은 큰 틀에서 작은 틀로 
o(log n)의 시간 복잡도를 가지고 있다고 생각.
-> 한번의 재귀 호출은 4번의 재귀호출을 불러옴 다만 탐색의 범위는 1/4로 점점 줄어듬
-> 범위가 점차적으로 감소, 또한 해당 탐색 범위의 감소 형태는 이진탐색트리에서의 방식과 비슷하다고 생각
-> 따라서 시간복잡도는 log n의 형태라 생각하였다.
'''


def recur(N, x, y):
    global ans

    if x == r and y == c:
        print(ans)
        exit(0)

    # 해당 사분면이 조건에 따라 값을 구해준다.
    # n == 1인 경우 해당 칸의 갯수만 더해준다.
    if N == 1:
        ans += 1
        return
    if not (x <= r < x + N and y <= c < y + N):
        ans += N * N
        return

    # 사분면 각 부분에 재귀호출 시작
    temp = N // 2
    recur(temp, x, y)
    recur(temp, x, y + temp)
    recur(temp, x + temp, y)
    recur(temp, x + temp, y + temp)


N, r, c = map(int, input().split())
ans = 0
recur(2 ** N, 0, 0)
