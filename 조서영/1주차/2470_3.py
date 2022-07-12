# 2470, Gold 5
# https://www.acmicpc.net/problem/2470

import sys

N=int(sys.stdin.readline())
S=sorted(list(map(int,sys.stdin.readline().rstrip().split())))

#target값과 가장 가까운 값을 찾는다.
def search(S, start, end, target):
    high=end-1
    low=start
    minimum_diff=999999999999999
    
    while low<high:
        mid=(high+low)//2
        
        diff=target-S[mid]
        if abs(diff)<minimum_diff:
            minimum_diff=abs(diff)
        if diff==0:
            break
        elif diff>0: #target>S[mid]
            low=mid+1
        elif diff<0: #target<S[mid]
            high=mid

    return high

minimum_diff=999999999999999
a,b=0,len(S)
b_tmp=len(S)-1
for idx in range(len(S)-1):
    a_tmp=idx
    if a_tmp>=b_tmp:
        break
    b_tmp=search(S,idx+1,b_tmp+1, -S[(a_tmp)])

    total=S[a_tmp]+S[b_tmp]
    if abs(total)<minimum_diff:
        minimum_diff=abs(total)
        a,b=a_tmp,b_tmp
    

print(S[a],S[b])
