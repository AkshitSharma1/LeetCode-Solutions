class Solution {
public:
    int dp2(int i,int j,vector<vector<int>>& dp,vector<vector<int>>& triangle) {
        
        if (i>=triangle.size()) return 0;
        if (dp[i][j]!=-1e7) return dp[i][j];
        int tempCost = 1e7;
        for(int nextStep=j;nextStep<=j+1;nextStep++) {
            tempCost = min(tempCost,triangle[i][j]+dp2(i+1,nextStep,dp,triangle));
        }
        return dp[i][j]= tempCost;
    }
    int minimumTotal(vector<vector<int>>& triangle) {
        vector<vector<int>> dp(triangle.size()+1,vector<int>(triangle.size()+1,-1e7));
        return dp2(0,0,dp,triangle);

    }
};