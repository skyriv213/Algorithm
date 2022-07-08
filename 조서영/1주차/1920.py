# 1920, Silver 4
# https://www.acmicpc.net/problem/1920

import sys

N=int(sys.stdin.readline())
A=sorted(list(map(int, sys.stdin.readline().rstrip().split())))
M=int(sys.stdin.readline())
llist=list(map(int, sys.stdin.readline().rstrip().split()))

def binary_search(S, target):
    high=len(S)-1
    low=0

    while low<=high:
        mid=(high+low)//2
        n=S[mid]

        if n==target:
            return 1
        elif n>target:
            high=mid-1
        elif n<target:
            low=mid+1
    
    return 0

for i in llist:
    print(binary_search(A, i))