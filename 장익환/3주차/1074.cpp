/*
7월20일, 백준 1074번, https://www.acmicpc.net/problem/1074
*/

#include <iostream>
using namespace std;

int N, r, c;
int cnt = 0;
 
void find(int x_low, int y_low, int width) {
	if (width <= 2) {
		// 영역의 가로, 세로 길이가 2이면 z모양 순서대로 탐색해봄
		if (r == y_low && c == x_low) {
			cout << cnt;
		}
		cnt++;

		if (r == y_low && c == x_low + 1) {
			cout << cnt;
		}
		cnt++;

		if (r == y_low + 1 && c == x_low) {
			cout << cnt;
		}
		cnt++;

		if (r == y_low + 1 && c == x_low + 1) {
			cout << cnt;
		}
		cnt++;

		return;
	}

	int half_width = width / 2;

	// r과 c가 포함되는 영역을 발견할 때만 재귀호출
	if (r < y_low + half_width) {
		if(c < x_low + half_width) {
			find(x_low, y_low, half_width);
		}
		else {
			cnt += half_width * half_width; // 왼쪽 위 영역에 속하지 않으므로 그 영역에 속하는 원소 만큼 값을 더함 
			find(x_low + half_width, y_low, half_width);
		}
	}
	else {
		cnt += 2 * half_width * half_width; // 위에 두 영역에 속하지 않으므로 그 영역에 속하는 원소만큼 값을 더함
		if (c < x_low + half_width) {
			find(x_low, y_low + half_width, half_width);
		}
		else {
			cnt += half_width * half_width; // 왼쪽 아래 영역에 속하지 않으므로 그 영역에 속하는 원소 만큼 값을 더함 
			find(x_low + half_width, y_low + half_width, half_width);
		}
	}
}

int main(void) {
	cin >> N >> r >> c;

	int n = 1;
	for (int i = 0; i < N; i++) {
		n *= 2;
	}

	find(0, 0, n);
}
