class Solution {
public:
    int f(string &s1,string &s2,vector<vector<int>>&dp,int l,int r) {
        if(l==s1.size() || r==s2.size()) {
            if(l==s1.size()&&r==s2.size()) return 0;
            if(r==s2.size()) {
                int sum=0;
                for(int i=l;i<s1.size();i++) sum+=int(s1[i]);
                return sum;
            } else {
                int sum=0;
                for(int i=r;i<s2.size();i++) sum+=int(s2[i]);
                return sum;
            }
        }

        if(dp[l][r]!=-1) return dp[l][r];
        if(s1[l]==s2[r]) return dp[l][r] = f(s1,s2,dp,l+1,r+1);
        return dp[l][r]=min(
            int(s1[l])+f(s1,s2,dp,l+1,r),
            int(s2[r]) + f(s1,s2,dp,l,r+1)
        );

    }
    int minimumDeleteSum(string s1, string s2) {
        int l=0;
        int r =0;
        vector<vector<int>> dp(s1.length()+1,vector<int>(s2.length()+1,-1));
        return f(s1,s2,dp,l,r);
    }
};