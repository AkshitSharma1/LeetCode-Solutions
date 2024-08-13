class Solution {
public:
    int dfs(int r,int c,vector<vector<int>>& dp,vector<vector<int>>& matrix) {    
    if (dp[r][c]!=-1) return dp[r][c];
    vector<pair<int,int>> disp = {{1,0},{-1,0},{0,1},{0,-1}};
    int ans = -1;
    for(auto d:disp) {
        int r_new = r+d.first;
        int c_new = c+d.second;
        if(r_new>=0 && r_new<matrix.size() && c_new>=0 && c_new<matrix[0].size()) {
            if(matrix[r_new][c_new]>matrix[r][c] ) {
                int dist = 1+dfs(r_new,c_new,dp,matrix);
                ans = max(ans,dist);
            }
        }
    }
    if (ans==-1) {
        return dp[r][c]=1;
    }
    return dp[r][c]=ans;
    }
    int longestIncreasingPath(vector<vector<int>>& matrix) {
     int m = matrix.size();
     int n = matrix[0].size();
     vector<vector<int>> dp(m+1,vector<int>(n+1,-1));
     int ans=-1;
     for(int i=0;i<m;i++) {
        for(int j=0;j<n;j++) {
            if(dp[i][j]==-1) dfs(i,j,dp,matrix);
            ans = max(ans,dp[i][j]);
        }
     }   
     return ans;
    }
};