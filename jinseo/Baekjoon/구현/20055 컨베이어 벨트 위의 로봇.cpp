#include <iostream>
#include<queue>

using namespace std;

/*
1 2 3 4 5 6
6 1 2 3 4 5
5 6 1 2 3 4
4 5 6 1 2 3
3 4 5 6 1 2
2 3 4 5 6 1

up, down: 올리는 위치, 내리는 위치
로봇이 벨트 위에 있는지 여부를 확인하는 배열
내구도 관리하는 배열 (Durability)
로봇의 위치를 관리하는 큐 (robot)
1. 벨트 움직임 -> start, end 감소
2. 로봇이 움직임 -> 큐 순회 -> cur + 1 (내부도 감소)
3. 로봇을 올린다. -> 올리는 위치 내부도 감소
내부도 감소시 ans ++
4. k <= ans 종료
*/

int n, k, ans, up_pos, down_pos;
int durability[202];
queue<int> robots;
bool isRobot[202];

void move_belt(){
    up_pos--;
    if(up_pos == 0) up_pos = 2 * n;
    
    down_pos--;
    if(down_pos == 0) down_pos = 2 * n;
}

void move_robots(){
    int size = robots.size();
    
    for(int i = 0; i < size; i++){
        // 큐를 순회해야하므로 pop시킴
        int cur_pos = robots.front(); robots.pop();
        
        if(cur_pos == down_pos) {
            isRobot[cur_pos] = false;
            continue;
        }
        
        int next_pos = cur_pos + 1;
        if(next_pos > 2 * n) next_pos = 1;
        
        // 만약 다음 칸으로 갈 수 있다면
        if(!isRobot[next_pos] && durability[next_pos] > 0){
            isRobot[cur_pos] = false;
            isRobot[next_pos] = true;
            durability[next_pos]--;
            
            if(durability[next_pos] == 0) ans++;
            
            // 다음으로 간 칸이 내린 지점이라면 큐에 푸쉬 x
            if(next_pos == down_pos){
                isRobot[next_pos] = false;
                continue;
            }
            
            robots.push(next_pos);
        }else{
            // 만약 현재 칸에 머물러 있다면
            robots.push(cur_pos);
        }
        
    }
}

void make_robot(){
    // 올리는 위치에 로봇이 있는지도 확인하지 않아도 됨
    if(durability[up_pos] > 0) {
        isRobot[up_pos] = true;
        durability[up_pos]--;
        robots.push(up_pos);
        if(durability[up_pos] == 0) ans++;
    }
}

int main()
{
    cin >> n >> k;
    
    for(int i = 1; i <= 2 * n; i++){
        cin >> durability[i];
    }
    
    up_pos = 1, down_pos = n;
    int cnt = 0;
    while(ans < k){
        cnt++;
        
        // 1. 벨트 움직임
        move_belt();
        
        // 2. 로봇이 움직임
        move_robots();
        
        // 3. 로봇 올리기
        make_robot();
    }
    
    cout << cnt;
    

    return 0;
}
