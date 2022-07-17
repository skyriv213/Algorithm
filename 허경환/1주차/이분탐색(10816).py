#파이썬 이진탐색 라이브러리 bisect 사용을 위한 import
from bisect import bisect_left

# 입력
n = int(input())
card_num = list(map(int, input().split()))
m = int(input())
tar_num = list(map(int, input().split()))

#숫자카드에 적혀있는 정수 중복제거
set_card_num = set(card_num)

# 딕셔너리 - key : 숫자카드에 적혀있는 숫자, value : 해당 숫자의 카드 소유 개수
tmp = {}
for i in set_card_num:
    tmp[i] = 0
for i in card_num:
    tmp[i] += 1

# 딕셔너리 키 기준 오름차순 정렬
s_tmp = sorted(tmp.items())
key_tmp = list(i[0] for i in s_tmp)
value_tmp = list(i[1] for i in s_tmp)

# 이진탐색으로 tar_num의 개수 찾기
for i in tar_num:
    # 가지고 있는 숫자카드 정수이면=집합에 해당 값이 있다면
    if i in set_card_num:
        # bisect_left로 key_tmp에서 i의 인덱스를 찾고, 같은 인덱스를 가지는 value_tmp의 값을 출력
        print(value_tmp[bisect_left(key_tmp, i)], end=' ')
    # 가지고 있는 숫자카드 정수가 아니면
    else:
        # 0을 출력
        print(0, end=' ')