class Solution {
public:
int f(vector<vector<int>>& dp,int l,int r,string& s) {
    if(r<=l) return 0;
    if(dp[l][r]!=-1) return dp[l][r];
    if(s[l]==s[r]) {
        return dp[l][r]=0+f(dp,l+1,r-1,s);
    } else {
        return dp[l][r]=1+min(f(dp,l+1,r,s),f(dp,l,r-1,s));
    }
}
    int minInsertions(string s) {
        int l=0;
        int n = s.size();
        int r = n-1;
        vector<vector<int>> dp(r+1,vector<int>(r+1,-1));
        return f(dp,l,r,s);
        
    }
};