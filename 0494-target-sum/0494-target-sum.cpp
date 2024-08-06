class Solution {
public:
    int f(vector<int>& nums, vector<vector<int>>& dp, int target, int index) {
        if (index == nums.size()) {
            return target == 0;
        }
        if (dp[index][target + 3000] != -1) {
            return dp[index][target + 3000];
        }
        return dp[index][target + 3000] = f(nums, dp, target + nums[index], index + 1) + f(nums, dp, target - nums[index], index + 1);
    }

    int findTargetSumWays(vector<int>& nums, int target) {
        int n = nums.size();
        vector<vector<int>> dp(n, vector<int>(5001, -1)); // 2001 to handle target range from -1000 to 1000
        return f(nums, dp, target, 0);
    }
};
