/*
백준 2470, https://www.acmicpc.net/problem/2470
*/

#include <iostream>
#include <algorithm>
using namespace std;

int liquid[100000];

// 절댓값을 구하는 함수
int absolute(int x) {
	return (x > 0) ? x : -x;
}

int main(void) {
	int N;
	int diff = 2123456789; // 0과의 혼합결과 사이의 차이 중 최솟값
						   // 두 용액을 합쳐도 절댓값이 2억을 넘지 않으므로 그보다 큰 값으로 초기화
	int liq1, liq2;        // 솔루션에 해당하는 두 용액의 특성값. 
						   // liq1에 인덱스가 더 작은 용액을 저장해야 출력이 오름차순임.
	int recent_diff;       // 최근까지 찾은 0과의 차이값

	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> liquid[i];
	}

	sort(liquid, liquid + N);

	// 특성값이 작은 용액부터 다른 용액들과 혼합해나감
	// 동일한 값을 더하기 때문에 배열의 원소들 사이에 순서관계는 변하지 않음!
	// 서로 다른 두 용액을 합쳤을때, 처음으로 0 이상인 경우와 0 미만인 경우를 확인함 
	for (int i = 0; i < N - 1; i++) {
		// 살펴봐야할 배열의 부분은 i + 1 ~ N - 1 범위임
		int left = i; // 자기 자신과 혼합하는 경우는 제외
		int right = N; // 처음으로 0이상인 위치가 됨
		int mid;

		// lower bound
		// 혼합할 때 처음으로 0 이상인 위치를 찾기
		while (left + 1 < right) {
			mid = (left + right) / 2;
			//cout << "mid: " << mid << "\n";

			if (liquid[mid] + liquid[i] >= 0) {
				right = mid;
			}
			else {
				left = mid;
			}
		}

		if (right >= N) { // right가 배열의 인덱스 범위를 넘어선다면
			// 확인해본 값들이 모두 0보다 작았다는 의미임
			// 확인한 값 중 제일 큰 값이 0과 제일 가까운지 확인 
			recent_diff = absolute(liquid[i] + liquid[N - 1]);
			if (recent_diff < diff) {
				diff = recent_diff;
				liq1 = liquid[i];      
				liq2 = liquid[N - 1];
			}
		}
		else { // right가 인덱스 범위 안에 있다면 
			// 혼합한 결과가 처음으로 0 이상인 값이 0에 제일 가까운지 확인
			recent_diff = absolute(liquid[i] + liquid[right]);
			if (recent_diff < diff) {
				diff = recent_diff;
				liq1 = liquid[i];
				liq2 = liquid[right];
			}
		}
		if (right - 1 > i) { // left - 1이 i보다 크다면
			// 혼합한 결과가 마지막으로 0 미만인 값이 0에 제일 가까운지 확인
			recent_diff = absolute(liquid[i] + liquid[right - 1]);
			if (recent_diff < diff) {
				diff = recent_diff;
				liq1 = liquid[i];
				liq2 = liquid[right - 1];
			}
		}
	}

	cout << liq1 << ' ' << liq2 << "\n"; // 인덱스가 더 작은 용액이 먼저 출력되므로 출력 결과는 오름차순임.
}
