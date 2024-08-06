class Solution {
public:
    bool f(vector<int>&nums,vector<vector<int>>& dp,int target,int index) {
        if(target<0) return false;
        if(target==0) return true;
        if(index==nums.size()-1) {
            return (nums[index]==target);
        }
        if(dp[index][target]!=-1) return dp[index][target];
        return dp[index][target] = f(nums,dp,target,index+1) || f(nums,dp,target-nums[index],index+1);
    }
    bool canPartition(vector<int>& nums) {
        long long sum=0;
        for(auto num:nums) sum+=num;
        if(sum%2==1) return false;
        sum/=2;
        int n = nums.size();
        vector<vector<int>> dp(n+1,vector<int>(sum+1,-1));
        return f(nums,dp,sum,0);
        

    }
};