class Solution {
public:
    int f(vector<vector<int>>&dp,string& s,int l,int r) {
        if(r<l) return 0;
        if(r==l) return 1;
        if(dp[l][r]!=-1) return dp[l][r];
        if(s[l]==s[r]) {
            dp[l][r] = 2+f(dp,s,l+1,r-1);
        } else {
            dp[l][r] = max(f(dp,s,l+1,r),f(dp,s,l,r-1));
        }
        return dp[l][r];
    }
    int longestPalindromeSubseq(string s) {
        int r = s.length()-1;
        int l =0;
        vector<vector<int>> dp(r+2,vector<int>(r+2,-1));
        return f(dp,s,l,r);
    }
};