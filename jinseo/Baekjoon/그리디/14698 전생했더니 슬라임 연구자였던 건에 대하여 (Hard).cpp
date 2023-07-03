#include <iostream>
#include <queue>
#define ll long long
#define MODN 1000000007

using namespace std;

ll slimes[61];

int main()
{
    
    int T;
    scanf("%d", &T);
    
    while(T--){
        int answer = 1;
        int N; cin >> N;
        
        priority_queue<ll> pq;
        
        for(int i = 0; i < N; i++){
            scanf("%lld", &slimes[i]);
            
            pq.push(-slimes[i]);
        }
        
        while(pq.size() >= 2){
            ll first = -pq.top(); pq.pop();
            ll second = -pq.top(); pq.pop();
            ll tmp = (first % MODN * second % MODN) % MODN;
            
            pq.push(-tmp % MODN);
            
            answer *= tmp % MODN;
        }
        
        printf("%d", answer);
        
    }
    
    return 0;
}
