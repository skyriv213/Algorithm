# 16571, Gold 3
# https://www.acmicpc.net/problem/16571
# col: 열, row=행
import sys
from copy import deepcopy

player={"X":1,"O":2}
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

result=[]
def play_game(board, player_flag, win_flag):
    ##보드의 모든 곳에 말이 놓여져 있으면 종료, 무승부
    if "W" in result:
        return 

    exit_flag=1
    for i in range(3):
        for j in range(3):
            if board[i][j]==0:
                B=deepcopy(board)
                B[i][j]=player[player_flag]
                if check(B, i, j):
                    if player_flag==win_flag:
                        result.append("W")
                        return

                if player_flag=="X":
                    if check_optimal(B, "O")==True:
                        play_game(B, "O", win_flag)
                else:
                    if check_optimal(B, "X")==True:
                        play_game(B, "X", win_flag)
   
    if exit_flag==1:
        result.append("D")
      
def check(B, row, col):
    if B[row][0]==B[row][1]==B[row][2] and B[row][0]!=0:
        return True
    if B[0][col]==B[1][col]==B[2][col] and B[0][col]!=0:
        return True
    if (B[0][0]==B[1][1]==B[2][2] and B[1][1]!=0) or (B[0][2]==B[1][1]==B[2][0] and B[1][1]!=0):
        return True
    return False

def check_optimal(B, target):
    for i in range(3):
        for j in range(3):
            if board[i][j]==0:
                B=deepcopy(board)
                B[i][j]=player[target]
                if check(B, i, j)==True:
                    return False    
    return True

if X_cnt<=O_cnt:
    play_game(board, "X", "X")
else:
    play_game(board, "O", "O")

if "W" in result:
    print("W")
elif "D" in result:
    print("D")
else:
    print("L")
    