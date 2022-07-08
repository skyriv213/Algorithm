# 13397, Gold 4
# https://www.acmicpc.net/problem/13397
# 최적화 문제를 결정 문제로 바꿔서 푸는 파라메트릭 서치 문제
# 최적화문제: 0~N의 배열을 모두 방문해서 각 구간 점수를 구하여 최솟값을 반환한다.
# 결정문제: 0~N의 배열을 모두 방문해서 구간 점수가 mid보다 큰 값을 포함한 구간 집합의 수가 m보다 큰지 여부를 반환한다.

import sys
INF=99999999999999

N,M=map(int, sys.stdin.readline().split())
S=list(map(int,sys.stdin.readline().rstrip().split()))

def solve(mid):
    cnt=1
    minV=INF
    maxV=-INF
    for i in range(len(S)):
        minV=min(minV, S[i])
        maxV=max(maxV, S[i])
        
        if (maxV-minV)>mid:
            cnt+=1
            minV=S[i]
            maxV=S[i]
    return cnt

high=max(S)
low=0
while low<high:
    mid=(high+low)//2

    if solve(mid)<=M:
        high=mid
    else:
        low=mid+1
    
print(high)