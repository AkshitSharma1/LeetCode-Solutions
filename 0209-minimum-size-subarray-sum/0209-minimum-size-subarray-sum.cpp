class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int i=0;
        int j=0;
        int n = nums.size();
        int calc_sum=0;
        int ans=INT_MAX;
        while(j<n) {
            calc_sum+=nums[j];
            while(i<=j&& calc_sum>=target) {
                ans = min(ans,j-i+1);
                calc_sum-=nums[i];
                i++;
            }
            j++;

        }
        return ans==INT_MAX?0:ans;
    }
};