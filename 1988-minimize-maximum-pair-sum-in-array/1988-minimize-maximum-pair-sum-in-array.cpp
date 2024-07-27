class Solution {
public:
    int minPairSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int n = nums.size();
        int l=0;
        int r = n-1;
        int maxSum=INT_MIN;
        while(l<r) {
            maxSum = max(maxSum,nums[l]+nums[r]);
            l+=1;
            r-=1;
        }
        return maxSum;
    }
};