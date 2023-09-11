#include<iostream>
#include<vector>
#include<algorithm>
#include<climits>

using namespace std;

int n, k;
vector<int> v;
int prefix_sum[100001];
int answer = INT_MIN;

int main(){
    cin >> n >> k;

    for(int i = 0; i < n; i++){
        int x; cin >> x; v.push_back(x);
    }

    for(int i = 0; i < n; i++){
        prefix_sum[i + 1] = v[i] + prefix_sum[i];
    }

    for(int i = k; i <= n; i++){
        answer = max(answer, prefix_sum[i] - prefix_sum[i - k]);
    }

    cout << answer;
}