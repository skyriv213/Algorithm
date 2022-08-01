/*
백준 1010번, https://www.acmicpc.net/problem/1010
*/

#include <iostream>
#include <vector>
#include <utility>
using namespace std; 

int memo[30][30]; // 메모이제이션을 위한 배열

// 다리를 놓는 경우의 수를 구하는 함수
int calc_case(int n, int m) {
	if (n > m) {  // 존재할 수 없는 경우
		return 0;
	}
	if (n == 1) { // 서쪽에 1개의 사이트만 있는 경우
		return m;
	}
	if (n == m) { // 서쪽와 동쪽에 동일한 수의 사이트가 있는 경우
		return 1;
	}

	if (memo[n][m] != -1) { // 이미 값을 구한 경우라면
		return memo[n][m];  // 저장된 값을 반환
	}

	// 동쪽에 있는 m개의 사이트 중에서 맨 위에 것을 고른 경우와 그 곳을 고르지 않은 경우를 더함
	return memo[n][m] = calc_case(n - 1, m - 1) + calc_case(n , m - 1);
}

int main(void) {
	vector<pair<int, int>> v;
	int T;
	int N, M;

	// 입력 받기
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> N >> M;
		v.push_back(make_pair(N, M));
	}

	// 각 테스트 케이스 별로 결과 출력
	for (int t = 0; t < T; t++) {
		// 메모이제이션을 위한 배열 초기화
		for (int i = 0; i < 30; i++) {
			for (int j = 0; j < 30; j++) {
				memo[i][j] = -1;
			}
		}

		cout << calc_case(v[t].first, v[t].second) << "\n";
	}
}

