class Solution {
public:

    int checkPallindrome(string&s ,int l,int r) {
        while(l<=r) {
            if(s[l++]!=s[r--]) return false;
        }
        return true;
    }
    int f(vector<vector<int>>& dp,string& s,int ind,int r) {
        if(ind>r) return 1e7;
        if(ind>=s.size()) return 1e7;
        if (dp[ind][r]!=-1) return dp[ind][r];
        if(checkPallindrome(s,ind,r)) return 0;
        int ans=INT_MAX;
        for(int i=ind;i<r;i++) {
            if(checkPallindrome(s,ind,i)) {
                //Its a pallindrome. check the next string
                ans =  min(ans,f(dp,s,i+1,r));
            }

        }
        return dp[ind][r]=ans+1;



    }
    int minCut(string s) {
        int n = s.length();//+1;
        vector<vector<int>> dp(n+1,vector<int>(n+1,-1));
        return f(dp,s,0,s.length()-1);


    }
};