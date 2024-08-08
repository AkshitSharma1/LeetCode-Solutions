class Solution {
public:
int f(vector<vector<int>>&dp,string& text1,string& text2,int n,int m,int i,int j) {
        if(i==n||j==m) {
            return 0;
        }
        if(dp[i][j]!=-1) return dp[i][j];
        return dp[i][j]=(text1[i]==text2[j])?1+f(dp,text1,text2,n,m,i+1,j+1):
        max(f(dp,text1,text2,n,m,i+1,j+1),max(f(dp,text1,text2,n,m,i+1,j),f(dp,text1,text2,n,m,i,j+1)));
    }
    int minDistance(string word1, string word2) {
          int n = word1.size();
        int m = word2.size();
        vector<vector<int>> dp(n+1,vector<int>(m+1,-1));
        int ans= f(dp,word1,word2,n,m,0,0);
        return (m-ans)+(n-ans);
    }
};