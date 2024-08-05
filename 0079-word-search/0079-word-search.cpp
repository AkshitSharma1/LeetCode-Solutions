class Solution {
public:
    bool solve(vector<vector<char>>& board, string& word, int pointer, int i, int j, int n, int m, vector<vector<bool>>& visited,vector<vector<int>>& dir) {
        if (pointer == word.size()) return true;
        if (i < 0 || i >= n || j < 0 || j >= m || board[i][j] != word[pointer] || visited[i][j]) return false;
        visited[i][j] = true;
        for (auto d : dir) {
            if (solve(board, word, pointer + 1, i+d[0], j+d[1], n, m, visited,dir)) {
                return true;
            }
        }
        visited[i][j] = false;
        return false;
    }

    bool exist(vector<vector<char>>& board, string word) {
        int n = board.size();
        int m = board[0].size();
                vector<vector<int>> dir = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        vector<vector<bool>> visited(n, vector<bool>(m, false));
        unordered_map<char,int> mp;
        for(auto r:board) {
            for(auto c:r) mp[c]++;
        }
        for(auto c:word) {
            mp[c]-=1;
            if(mp[c]<0) return false;
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (solve(board, word, 0, i, j, n, m, visited,dir)) return true;
            }
        }
        return false;
    }
};
