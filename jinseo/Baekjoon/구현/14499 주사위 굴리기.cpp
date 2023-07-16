// 칸이 0이면, 주사위의 바닥면에 쓰여있는 수가 칸에 복사
// 칸이 0이 아니면, 칸에 쓰여있는 수가 주사위의 바닥면에 복사되며, 칸에 있는 수는 0이 된다.

#include <iostream>

using namespace std;

int n, m, x, y, k;
int _map[21][21];
int command;
int dice[7];

bool check_range(int y, int x){
    if(y >= n || x >= m || y < 0 || x < 0) return false;
    return true;
}

void copy_dice(int y, int x){
    if(_map[y][x] == 0){
        _map[y][x] = dice[6];
    }else{
        dice[6] = _map[y][x];
        _map[y][x] = 0;
    }
}

/*
동쪽 
  2
6 4 1
  5
  3
  
서쪽
  2
1 3 6 
  5
  4
  
북쪽
  1
4 5 3
  6
  2
  
남쪽
  6
4 2 3
  1
  5
*/

int main()
{
    cin >> n >> m >> y >> x >> k;
    
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> _map[i][j];
        }
    }
    
    for(int i = 0; i < k; i++){
        cin >> command;
        
        int tmp = dice[1];
        
        // 동쪽
        if(command == 1){
            if(!check_range(y, x + 1)) continue;
            
            dice[1] = dice[4];
            dice[4] = dice[6];
            dice[6] = dice[3];
            dice[3] = tmp;
            
            x++;
            copy_dice(y, x);
        }
        // 서쪽
        else if(command == 2){
            if(!check_range(y, x - 1)) continue;
            
            dice[1] = dice[3];
            dice[3] = dice[6];
            dice[6] = dice[4];
            dice[4] = tmp;
            
            x--;
            copy_dice(y, x);
            
        }
        // 북쪽
        else if(command == 3){
            if(!check_range(y - 1, x)) continue;
            
            dice[1] = dice[5];
            dice[5] = dice[6];
            dice[6] = dice[2];
            dice[2] = tmp;
            
            y--;
            copy_dice(y, x);
        }
        // 남쪽
        else if(command == 4){
            if(!check_range(y + 1, x)) continue;
            
            dice[1] = dice[2];
            dice[2] = dice[6];
            dice[6] = dice[5];
            dice[5] = tmp;
            
            y++;
            copy_dice(y, x);
        }
        else continue;
        
        cout << dice[1] << "\n";
    }
    

    return 0;
}
