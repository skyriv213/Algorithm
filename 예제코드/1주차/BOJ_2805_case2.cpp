#include <iostream>
using namespace std;
typedef long long int ll;

ll max(ll a, ll b){
    return a>b?a:b;
}

ll F(ll* v, ll x, ll n) {
	ll sum = 0;
	for (int i = 0; i < n; ++i) {
		ll get_wood = max(v[i]-x, 0) ;
		sum += get_wood;
	}
	return sum;
}

bool G(ll* v, ll x, ll n, ll m) {
	return F(v, x, n) >= m;
}

int main() {
	ll* v;
	ll N, right = 0, left = 0, ans = 0, M;
	cin >> N >> M;
	v = new ll[N];
	for (int i = 0; i < N; ++i) {
		cin >> v[i];
        right=max(right,v[i]);
	}
	left = -1;
	++right;
	//불변식 1 left<right
	//불변식 2 G(left) = true, G(right)=false -> F(left)>F(right)
	while (left + 1 < right) {
		ll mid = (left + right) / 2;
		if (G(v,mid,N,M)) {
			left = mid;
		}
		else {
			right = mid;
		}
	}
	cout << left;
	return 0;
}
