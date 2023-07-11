#include<iostream>
#include<string>
#include<algorithm>

using namespace std;

string s;

bool check(int i){
    int h = (s.size() - i) / 2;

    for(int idx = 0; idx < h; idx++){
        if(s[idx + i] != s[s.size() - 1 - idx]) return false;
    } 
    return true;
}

int main(){
    cin >> s;

    for(int i = 0; i < s.size(); i++){
        if(check(i)){
            cout << s.size() + i;
            return 0;
        }
    }
}