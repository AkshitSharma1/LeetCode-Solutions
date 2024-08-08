class Solution {
public:
int f(vector<vector<int>>& dp,vector<int>& nums,int prev,int i) {
    if(i==nums.size()) return 0;
    if(dp[i][prev+1]!=-1) return dp[i][prev+1];
    int pick=0;
    int npick=0;
    if(prev==-1 || nums[i]>nums[prev]) {
        pick = 1 + f(dp,nums,i,i+1);
    }
    npick = 0 + f(dp,nums,prev,i+1);
    return dp[i][prev+1] = max(pick,npick);
}
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> dp(n+1,vector<int>(n+1,-1));
        return f(dp,nums,-1,0);
    }
};