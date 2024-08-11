class Solution {
public:
    int f(vector<vector<int>>& dp, string& word1, string& word2, int l, int r, int m, int n) {
        if (r == word2.size()) {
            if (l == word1.size()) return 0;
            return word1.size() - l;
        }
        if (l == word1.size()) {
            return word2.size() - r;
        }
        if (dp[l][r] != -1) return dp[l][r];
        
        if (word1[l] == word2[r]) return dp[l][r] = f(dp, word1, word2, l + 1, r + 1, m, n);
        
        int insertOpCount = 1 + f(dp, word1, word2, l, r + 1, m, n);
        int deleteOpCount = 1 + f(dp, word1, word2, l + 1, r, m, n);
        int replaceOpCount = 1 + f(dp, word1, word2, l + 1, r + 1, m, n);
        
        return dp[l][r] = min({insertOpCount, deleteOpCount, replaceOpCount});
    }
    
    int minDistance(string word1, string word2) {
        int m = word1.size();
        int n = word2.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, -1));
        return f(dp, word1, word2, 0, 0, m, n);
    }
};
