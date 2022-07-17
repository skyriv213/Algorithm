from bisect import bisect_left

# 입력
n = int(input())
arr = list(map(int, input().split()))

# 특성값 오름차순 정렬
arr.sort()

# 특성값의 최솟값, 최댓값 구하기
max_num = max(arr)
min_num = min(arr)

# 모두 산성 용액인 경우
if min_num > 0:
    print(arr[0], arr[1])
# 모두 알칼리성 용액인 경우
elif max_num < 0:
    print(arr[-2], arr[-1])
# 산성, 알칼리성 둘다있는 경우
else:
    # 두 용액의 특성값을 저장할 리스트
    ls = []
    # 두 용액의 특성값의 합
    answer = 2000000000
    # arr리스트의 요소 i에 대하여 더했을 때 특성값이 가장 0에 가까운 요소 tmp찾기
    tmp = 0
    for i in arr:
        b_index = bisect_left(arr, -i)
        if b_index == 0:
            tmp = arr[0]
        elif b_index == n:
            tmp = arr[-1]
        else:
            if arr[b_index - 1] == i:
                tmp = arr[b_index]
            elif arr[b_index] == i:
                tmp = arr[b_index - 1]
            elif abs(arr[b_index] - i) < abs(arr[b_index - 1] - i):
                tmp = arr[b_index]
            else:
                tmp = arr[b_index - 1]

        abs_num = abs(i + tmp)
        if abs_num < answer:
            ls = [i, tmp]
            answer = abs_num
    ls.sort()
    print(ls[0], ls[1])