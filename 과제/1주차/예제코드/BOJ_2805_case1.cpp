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
	left = 0;
	//불변식 1 left-1<=right
	//불변식 2 G(left-1) = true, G(right+1)=false -> F(left-1)>F(right+1)
	while (left <= right) {
		ll mid = (left + right) / 2;
		if (G(v,mid,N,M)) {
			left = mid+1;
		}
		else {
			right = mid-1;
		}
	}
	cout << right;
	delete[] v;
	return 0;
}
