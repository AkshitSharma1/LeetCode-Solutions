class Solution {
public:
    int dfs(vector<vector<char>>& board,int r, int c) {
        if (r>=board.size() || r<0 || c<0 || c>=board[0].size()) return 0;
        if (board[r][c]=='B') return 0;
        if (board[r][c]=='M') return 1;
        if (board[r][c]=='E') {
            board[r][c]='B'; //for the time being
            //We will have to update the count
            int adjMineCount=0;
            for(int dr=-1;dr<=1;dr++) {
                for(int dc=-1;dc<=1;dc++) {
                    if (r+dr>=board.size() || r+dr<0 || c+dc<0 || c+dc>=board[0].size()) continue;
                    if (board[r+dr][c+dc]=='M') adjMineCount++;
                    
                }
            }
            if(adjMineCount==0) {
                board[r][c]='B';
                 for(int dr=-1;dr<=1;dr++) {
                for(int dc=-1;dc<=1;dc++) {
                   dfs(board,r+dr,c+dc);
                }
            }
            } else {
                board[r][c]= adjMineCount+'0';
            }
        }
        return 0;
    }
    vector<vector<char>> updateBoard(vector<vector<char>>& board, vector<int>& click) {
        int rClick = click[0];
        int cClick = click[1];
       // vector<vector<int>> visited(board.size()+1,vector<int>(board.size()+1,-1));
        if (board[rClick][cClick]=='M') {
            board[rClick][cClick]='X';
            return board;
        } else {
            //Its E
            //Apply DFS To update it
            dfs(board,rClick,cClick);
        }
        return board;
    }
};