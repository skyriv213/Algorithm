/*
백준 11726번, https://www.acmicpc.net/problem/11726
*/

// 분할 정복으로 구하려고 하니 익숙한 재귀식인 피보나치 수열을 발견함
// 반복되는 계산을 줄이려면 메모이제이션을 이용한 동적 프로그래밍을 이용하는 것이 좋음

#include <iostream>
using namespace std;

int memo[1001]; // 메모이제이션을 위한 배열

// 가로가 width이고 세로가 2인 직사각형에 타일을 놓는 경우의 수를 구하는 함수
int find(int width) {
	if (width < 0) { // 너비가 음수가 되었다면 
		return 0;    // 채울 수 없는 경우임
	}
	if (width == 0) { // 너비가 0이 되면
		return 1;     // 채울 수 있는 경우를 찾았음
	}

	if (memo[width] != -1) { // 이미 경우의 수를 구했다면 
		return memo[width];  // 바로 리턴 
	}

	// 세로로 타일을 놓은 경우의 수와 가로로 타일을 놓은 경우의 수를 더해서 경우의 수를 구함
	return memo[width] = ((find(width - 1) % 10007) + (find(width - 2) % 10007)) % 10007; 
}

int main(void) {
	int N;
	
	cin >> N;

	// 메모이제이션을 위한 배열 초기화
	for (int i = 1; i <= 1000; i++) {
		memo[i] = -1;
	}

	cout << find(N);
}

