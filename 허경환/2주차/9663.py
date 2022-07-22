#n-queen
#입력
n = int(input())
#퀸을 놓는 방법의 수
ans = 0
#퀸을 놓은 위치 표시
row = [0] * n

#유망한지 파악. 즉, 일직선상과 대각선상에 다른 퀸이 있는지 파악
#(x,y)의 대각선에 위치한 좌표(a,b)는 abs(x-a)==abs(y-b)를 만족한다.
def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

#dfs
def n_queens(x):
    global ans
    #놓은 퀸이 n개라면
    if x == n:
        ans += 1
        return
    #놓은 퀸이 n개가 아니라면
    else:
        #만약 (x,i)자리에 퀸을 놓는다면
        for i in range(n):
            row[x] = i
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print(ans)

