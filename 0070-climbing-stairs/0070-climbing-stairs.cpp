class Solution {
public:
    int f(vector<int>& dp,int step,int n) {
        if(step>n) return 0;
        if(step==n) return 1;
        if(dp[step]!=-1) return dp[step];
        return dp[step]=f(dp,step+1,n) + f(dp,step+2,n);
    }
    int climbStairs(int n) {
        vector<int> dp(n,-1);
        return f(dp,0,n);
    }
};