/*
백준 15651번, https://www.acmicpc.net/problem/15651
*/
#include <iostream>
using namespace std;

int N, M;
int seq[7];   // 수열을 저장할 배열

void find_sequence(int k) {
	if (k == M) {             // 레벨이 M이 되면 
		// 수열을 찾았으므로 출력
		for (int i = 0; i < M; i++) {
			cout << seq[i] << ' ';
		}
		cout << "\n";
		return; 
	}

	// 중복해서 선택할 수 있으므로 1 ~ N 중에서 선택
	for (int i = 1; i <= N; i++) {
		seq[k] = i;          
		find_sequence(k + 1);
	}
}

int main(void) {
	cin >> N >> M;
	
	find_sequence(0);
}
