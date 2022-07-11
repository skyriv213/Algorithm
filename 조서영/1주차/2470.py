# 2470, Gold 5
# https://www.acmicpc.net/problem/2470

import sys

N=int(sys.stdin.readline())
S=sorted(list(map(int,sys.stdin.readline().rstrip().split())))

high=len(S)-1
low=0
minimum_diff=9999999999999999
a,b=0,0
while low<high:
    highV=S[high]
    lowV=S[low]

    diff=highV+lowV
    if minimum_diff>abs(diff):
        minimum_diff=abs(diff)
        a,b=lowV,highV
    if diff==0:
        a,b=lowV,highV
        break
    elif diff>0:
        high-=1
    else:
        low+=1

print(a,b)
