class Solution {
public:
  int f(vector<int>& dp,int step,vector<int>& cost) {
        if(step>cost.size()) return INT_MAX;
        if(step==cost.size()) return 0;
        if(dp[step]!=-1) return dp[step];
        return dp[step]=cost[step]+min(f(dp,step+1,cost),f(dp,step+2,cost));
    }
    int minCostClimbingStairs(vector<int>& cost) {
        vector<int> dp(cost.size()+1,-1);
        return min( f(dp,0,cost),f(dp,1,cost));
    }
};