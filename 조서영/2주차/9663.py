# 9663, Gold 4
# https://www.acmicpc.net/problem/9663

import sys

n=int(sys.stdin.readline())

cnt=0
S=[-1]*(n+1)
def func(idx):
    global cnt
    if idx==n:
        cnt=cnt+1
        return

    for i in range(1,n+1):
        S[idx+1]=i
        if promising(idx+1):
            func(idx+1)


def promising(idx):
    if idx==1:
        return True
    
    for i in range(1, idx, 1):
        if S[i]==S[idx] or abs(S[i]-S[idx])==abs(i-idx):
            return False
    return True       

func(0)
print(cnt)
