# 15651, Silver 3
# https://www.acmicpc.net/problem/15651

import sys

N,M=map(int,sys.stdin.readline().split())

S=[0 for i in range(M)]
def dfs(idx):
    if idx==M:
        print(' '.join(S))
        return  
    
    for i in range(1, N+1, 1):
        S[idx]=str(i)
        dfs(idx+1)

dfs(0)
