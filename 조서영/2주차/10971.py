# 10971, Silver2
# https://www.acmicpc.net/problem/10971

import sys
N=int(sys.stdin.readline())
costs=[list(map(int, sys.stdin.readline().rstrip().split())) for i in range(N)]

minimum_cost=100000000 
S=[0]+[-1]*(N-1)
def dfs(idx, cost):
    if idx==N:
        global minimum_cost
        if costs[S[idx-1]][0]!=0:
            cost+=costs[S[idx-1]][0]
            if cost<minimum_cost:
                minimum_cost=cost
        return 
    
    for i in range(N):
        if costs[S[idx-1]][i]!=0: #갈 수 없는 도시가 아닌 경우
            S[idx]=i
            if promising(idx): #이전에 방문한 노드가 아닌 경우
                dfs(idx+1, cost+costs[S[idx-1]][S[idx]])

#이전에 방문한 노드인가?
def promising(idx):
    for i in range(idx):
        if S[idx]==S[i]:
            return False
    return True

dfs(1, 0)
print(minimum_cost)
