/*
백준 1920번, https://www.acmicpc.net/problem/1920
*/

#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
	int N, M;
	int A[100000]; // N개의 정수 
	int key[100000]; // M개의 정수

	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> A[i];
	}

	cin >> M;
	for (int i = 0; i < M; i++) {
		cin >> key[i];
	}

	sort(A, A + N);

	for (int i = 0; i < M; i++) {
		// 이분 탐색으로 0인지 1인지 판정
		int left = -1;
		int right = N;
		int mid;

		while (left + 1 < right) {
			mid = (left + right) / 2;
			if (A[mid] < key[i]) {
				left = mid;
			}
			else {
				right = mid;
			}
		}
		if (A[right] == key[i]) {
			cout << "1\n";
		}
		else {
			cout << "0\n";
		}
	}
}
