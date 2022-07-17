'''
n개의 수를 입력 및 경우의 수를 점점 좁혀간다.
한번의 순환 구조를 찾으면 그 순서를 가지고 값을 구하면 된다.
도시에서 출발해 원래 도시로 돌아오는 경우의 최소 값을 구하면 된다
1234 혹은 2341 어떤 경우든 한번의 순서를 찾으면 값이 나오게 된다.

그래서 입력받은 그래프를 토대로 각각의 1번 도시에서 어느 도시로 가야 최소값이 나오는지
첫번째 순환에서 O(n)이 등장한다. 그리고 기존 도시를 제외하고 경우의 탐색을 진행해야한다.
탐색을 하는 도중 (n-1)!의 호출을 진행한다. 따라서 O(n!)이 된다.

'''

def dfs(now, tmp):
    global ans
    if tmp > ans:
        return
    if sum(check) == n - 1:
        if city[now][0] > 0:
            ans = min(ans, tmp + city[now][0])
        return

    for i in range(1, n):
        if city[now][i] and not check[i]:
            check[i] = True
            dfs(i, tmp + city[now][i])
            check[i] = False


n = int(input())
city = [list(map(int, input().split())) for i in range(n)]
check = [False for _ in range(n)]
tmp, ans = 0, 1e9

for i in range(1, n):
    if city[0][i]:
        check[i] = True
        dfs(i, city[0][i])
        check[i] = False

print(ans)

