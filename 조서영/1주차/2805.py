# 2805, Silver 2
# https://www.acmicpc.net/problem/2805
# 이분탐색

## 반례1
## 1 10
## 10
## 반례
## 2 11
## 10 10
import sys

N,M=map(int, sys.stdin.readline().split())
trees=list(map(int,sys.stdin.readline().rstrip().split()))

low=0
high=max(trees)
while low<=high:
    mid=(low+high)//2

    total_get=0
    for tree in trees:
        if tree-mid>0:
            total_get+=tree-mid

    if total_get>=M:
        low=mid+1
    else:
        high=mid-1

print(high)