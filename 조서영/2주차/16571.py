# 16571, Gold 3
# https://www.acmicpc.net/problem/16571
# col: 열, row: 행
import sys

player={1:1,-1:2}  #"X":1,"O":2
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

def game(board, player_flag):
    min_num=1
    
    dual_flag=1
    for i in range(3):
        for j in range(3):
            if board[i][j]==0:
                dual_flag=0
                board[i][j]=player[player_flag]
                if check(board, i, j, player[player_flag]):
                    min_num=min(min_num,-1)
                min_num=min(min_num, game(board, player_flag*-1)*-1)
                board[i][j]=0

    if dual_flag==1:
        min_num=min(min_num, 0)

    return min_num       


def check(B, row, col, win_flag):
    if B[row][0]==B[row][1]==B[row][2] and B[row][0]==win_flag:
        return True
    if B[0][col]==B[1][col]==B[2][col] and B[0][col]==win_flag:
        return True
    if (B[0][0]==B[1][1]==B[2][2] and B[1][1]==win_flag) or (B[0][2]==B[1][1]==B[2][0] and B[1][1]==win_flag):
        return True
    return False

if X_cnt<=O_cnt:
    result=game(board, 1)
else:
    result=game(board, -1)

if result==-1:
    print("W")
elif result==0:
    print("D")
elif result==1:
    print("L")

