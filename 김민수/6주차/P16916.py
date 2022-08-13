'''
16916
KMP 알고리즘 활용
'''
'''
kmp 알고리즘을 사용하여 접근하려하였다.
해당 알고리즘에는 두 가지의 메서드가 필요하다.
1. lps 접두/접미의 최대 길이를 저장하는 리스트를 만들어주는 메서드
2. lps는 kmp의 기준이 된다.

해당 알고리즘의 시간복잡도는 결론적으로는 text의 주어진 길이만큼만 탐색을 진행하기에
O(n)이라고 생각한다.

'''

# lps를 만드는 메서드이다
# lps의 경우 결국 하나씩 늘어나거나 혹은 초기화가 되면서 처음부터 진행이 되는 리스트이다.
# 이로인해 이 lps값을 그대로 인덱스의 값으로 사용할 수 있다고 생각을 하였다.
def make_lps(sub):
    arr = [0 for _ in range(len(sub))]
    j = 0
    for i in range(1, len(sub)):
        # sub의 경우
        while j > 0 and sub[i] != sub[j]:
            j = arr[j - 1]
        if sub[i] == sub[j]:
            j += 1
            arr[i] = j
    return arr


def kmp(text, sub):
    i = 0
    j = 0
    # 반복문 i가 text의 길이보다 작을때까지
    while i < len(text):
        # 해당 인덱스의 값이 같은 값일 경우 각 i,j를 1씩 증가
        if text[i] == sub[j]:
            i += 1
            j += 1
        # 만약 틀릴 경우
        elif text[i] != sub[j]:
            # 만약 j가 0이 아닌경우 j가 0이 될때까지 혹은 이전 lps를 통한 sub의 탐색으로 이전 문자열과 비교
            if j != 0:
                j = lps[j-1]
            # j가 0이면 i를 1씩 더 늘려서 text의 다음 문자를 탐색
           else:
                i += 1
        # 존재의 유무를 확인하는 문제이다. 따라서 j의 값이 해당 문자열의 값과 같아지면 true 출력
        if j == len(sub):
            return True

    return False

    # for문 사용 kmp search

    # for i in range(len(text)):
    #     while j > 0 and text[i] != sub[j]:
    #         j = lps[j - 1]
    #     if text[i] == sub[j]:
    #         if j == len(sub) - 1:
    #             j = lps[j]
    #             return True
    #         else:
    #             j += 1
    # return False


text = input().strip()
sub = input().strip()

lps = make_lps(sub)

ans = kmp(text, sub)

print(1 if ans else 0)
