'''
백준 16172
이전의 16916 문제와 똑같은 문제이다
다만 이 경우에는 처음 입력을 받는 문자에 숫자가 포함이 되어있어서
입력받은 초행을 다시 설정해줘야한다는 점이다. 그래서 리스트를 다시 입력할 경우
isalpha 메서드를 사용했다.
isalpha의 경우 문자열에 숫자 및 공백이 포함이 되면 False를 리턴하는 그러한 메서드이다.

나머지 코드의 부분은 기존 16916에서 가져왔다.
시간복잡도는 o(m + n)인것 같다.
기존 16916의 경우 결론적으로 n의 길이가 될때까지의 시간이 될것이라 생각하였지만 이번에 다시 한 번 ppt를 보며 찾아보니
매칭이 안되는 부분에서 주어진 k의 길이만큼 탐색을 하기에 이 부분도 추가가 되어야 하는 것 같다.

'''

def make_lps(k):
    i, j = 1, 0
    arr = [0 for _ in range(len(k))]

    while i < len(k):
        if k[i] == k[j]:
            j += 1
            arr[i] = j
            i += 1
        else:
            if j != 0:
                j = arr[j - 1]
            else:
                i += 1
    return arr


def kmp(ss, k):
    i, j = 0, 0
    while i < len(ss):
        # 성공 o(n) n은 ss의 길이
        if ss[i] == k[j]:
            j += 1
            i += 1
        # 실패 o(m) m은 k의 길이
        elif ss[i] != k[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
        if j == len(k):
            return True
    return False


s = input().strip()
k = input().strip()

ss = [i for i in s if i.isalpha()]
ss = "".join(ss)

lps = make_lps(k)

ans = kmp(ss, k)
print(1 if ans else 0)
