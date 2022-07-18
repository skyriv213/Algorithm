/*
백준 9663번, https://www.acmicpc.net/problem/9663
*/

#include <iostream>
#include <cstdlib>
using namespace std;

int queen_cols[15]; // 각 행에 있는 퀸이 위치한 열을 저장
int N;              
int cnt = 0;        // 퀸이 공격하지 않고 놓일 수 있는 경우의 수

void nqueen(int d) {

	if (d == N) {   // 레벨이 N이 되면 
		cnt++;      // 퀸들이 서로 공격하지 않고 놓일 수 있는 경우를 찾음
		return;
	}

	// d 행에서 퀸을 col 열에 배치함 
	for (int col = 0; col < N; col++) { 
		// 퀸을 col 열에 놓았을 때, 해답을 낼 수 있는지 확인
		bool flag = true;            // flag의 값에 따라서 다음 노드로 재귀할지 결정                
		for (int j = 0; j < d; j++) {
			if (queen_cols[j] == col || d - j == abs(queen_cols[j] - col)) {
				flag = false;
				break;
			}
		}
		
		if (flag) {
			queen_cols[d] = col; // d 행에 퀸을 col에 놓는 경우를 선택 
			nqueen(d + 1);       // 자식 노드로 이동
		}
	}

}

int main(void) {
	cin >> N;

	nqueen(0);
	
	cout << cnt;
}
