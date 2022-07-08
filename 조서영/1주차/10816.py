# 10816, Silver 4
# https://www.acmicpc.net/problem/10816

import sys

N=int(sys.stdin.readline())
A=list(map(int, sys.stdin.readline().rstrip().split()))
D=dict()
for i in A:
    if i not in D:
        D[i]=1
    else:
        D[i]+=1
    
M=int(sys.stdin.readline())
B=list(map(int, sys.stdin.readline().rstrip().split()))
result=[]
for i in B:
    if i in D:
        result.append(str(D[i]))
    else:
        result.append(str(0))

print(' '.join(result))