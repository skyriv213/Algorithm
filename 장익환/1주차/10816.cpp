/*
백준 10816번, https://www.acmicpc.net/problem/10816
*/

#include <iostream>
#include <algorithm>
using namespace std;

int cards[1000000]; // N개의 카드를 저장
int m_int[1000000]; // M개의 정수를 저장

int main(void) {
	int N, M;

	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> cards[i];
	}

	cin >> M;
	for (int i = 0; i < M; i++) {
		cin >> m_int[i];
	}

	sort(cards, cards + N);

	for (int i = 0; i < M; i++) {
		// 정렬된 배열에서 카드가 존재하는 인덱스의 범위를 구함.
		// 이를 위해서 lower bound와 upper bound를 이용함.
		int left = -1;
		int right = N;
		int mid, m_start, m_end;

		// lower bound
		while (left + 1 < right) {
			mid = (left + right) / 2;
			if (cards[mid] >= m_int[i]) {
				right = mid;
			}
			else {
				left = mid;
			}
		}
		m_start = right; // 처음으로 m_int[i] 이상의 수가 있는 위치 

		left = -1;
		right = N;
		// upper bound 
		while (left + 1 < right) {
			mid = (left + right) / 2;
			if (cards[mid] > m_int[i]) {
				right = mid;
			}
			else {
				left = mid;
			}
		}
		m_end = right; // 처음으로 m_int[i]을 초과하는 수가 있는 위치 

		cout << m_end - m_start << ' '; // 그 차이가 곧 m_int[i]의 갯수
	}
}