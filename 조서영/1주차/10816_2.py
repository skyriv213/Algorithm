# 10816, Silver 4
# https://www.acmicpc.net/problem/10816

import sys

N=int(sys.stdin.readline())
A=sorted(list(map(int, sys.stdin.readline().rstrip().split())))
M=int(sys.stdin.readline())
B=list(map(int, sys.stdin.readline().rstrip().split()))

def search_upperbound(S, target):
    high=len(S)
    low=0
    while low<high:
        mid=(high+low)//2
        
        if S[mid]<=target:
            low=mid+1
        elif S[mid]>target:
            high=mid
    
    return high

def search_lowerbound(S, target):
    high=len(S)
    low=0
    while low<high:
        mid=(high+low)//2
        
        if S[mid]>=target:
            high=mid
        elif S[mid]<target:
            low=mid+1
    
    return low

result=[]
for i in B:
    result.append(str(search_upperbound(A, i)-search_lowerbound(A, i)))

print(' '.join(result))