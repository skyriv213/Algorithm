/*
백준 5904번, https://www.acmicpc.net/problem/5904
*/

#include <iostream>
using namespace std;

// S(k)에서 i번째 문자가 무엇인지 출력하는 함수
// size는 S(k)의 길이 
void find(int k, int i, int size) { 
	if (k <= 0) { 
		// S(0)에서 i에 해당하는 문자 알아내기
		if (i == 0) {
			cout << "m";
		}
		else {
			cout << "o";
		}
		return;
	}

	// S(k)에서 i번째 문자가 어디에 있는지 결정함
	int bound = (size - (k + 3)) / 2;

	if (i < bound) {  // S(k)에서 앞에 있는 S(k-1)에 속한다면
		find(k - 1, i, bound);  // S(k-1)에서 어느 문자인지 알아내야함
	}
	else if (i < bound + k + 3) { // S(k)에서 중간에 있는 k+3개의 문자에 속한다면
		if (i == bound) {         // 즉시 알아낼 수 있음
			cout << "m";
		}
		else {
			cout << "o";
		}
		return;
	}
	else {             // S(k)에서 뒤에 있는 S(k-1)에 속한다면
		find(k - 1, i - (bound + k + 3), bound); // S(k-1)에서 어느 문자인지 알아내야함
	}
	
}

int main(void) {
	int N;
	cin >> N;

	int k, size, temp;
	
	// N번째 수가 존재하는 가장 작은 수열 S(k)의 길이 구하기
	size = temp = 3;
	k = 0;
	while (size < N) {
		k++;
		size = (k + 3) + 2 * temp;
		temp = size;
	}

	find(k, N - 1, size); // 수열에서 문자의 인덱스는 0부터 시작하므로 N-1을 입력으로 줌

	return 0;
}
