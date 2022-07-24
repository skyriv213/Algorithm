'''
아래에서 위로 진행
moo의 길이가 주어진 n을 넘어설때까지 반복. 문제의 경우 moo를 만드는 방법이 주어져있다.
이 경우의 문자열의 길이가 해당 길이를 만드는 함수의 반복에 따라 달라진다. 따라서 해당 메서드를
규정하는 k를 점차 증가시키면서 진행을 하였다.
시간복잡도의 경우 지속적인 재귀의 호출로 탐색범위는 점차적으로 줄어든다. 따라서 O(log(n)이라고 추정한다.
'''

n = int(input())

cnt = 0

m = ["m", 'o', "o"]

def moo(n, k, l):
    # moo 수열의 길이 탐색, 길이가 n을 넘어설 때까지 반복
    new_length = l * 2 + k + 3
    # n이 3 이하이면 정해진 리스트에서 출력
    if n <= 3:
        print(m[n - 1])
        return
    if new_length < n:
        moo(n, k + 1, new_length)
    else:
        if l < n <= l + k + 3:
            if n - l == 1:
                print("m")
            else:
                print("o")
            return
        else: # 앞에 moo는 볼 필요 없으니 순서 재정립 후 재 호출
            moo(n - (l + (k + 3)), 1, 3)


moo(n, 1, 3)
