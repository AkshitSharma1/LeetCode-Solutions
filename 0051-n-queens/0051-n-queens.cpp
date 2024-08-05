class Solution {
public:
    bool canPlaceQueen(vector<string>& temp, vector<pair<int, int>>& pos, int i, int j) {
        for (auto& p : pos) {
            if (p.first == i || p.second == j || abs(p.second - j) == abs(p.first - i)) return false;
        }
        return true;
    }

    void solve(int n, int row, vector<vector<string>>& results, vector<pair<int, int>>& pos, vector<string>& temp) {
        if (row == n) {
            results.push_back(temp);
            return;
        }

        for (int j = 0; j < n; j++) {
            if (canPlaceQueen(temp, pos, row, j)) {
                // Place the queen
                pos.push_back({row, j});
                temp[row][j] = 'Q';
                solve(n, row + 1, results, pos, temp);
                // Remove the queen
                pos.pop_back();
                temp[row][j] = '.';
            }
        }
    }

    vector<vector<string>> solveNQueens(int n) {
        vector<pair<int, int>> pos;
        vector<vector<string>> results;
        vector<string> temp(n, string(n, '.'));
        solve(n, 0, results, pos, temp);
        return results;
    }
};
