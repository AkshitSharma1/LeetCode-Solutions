class Solution {
public:
    int numSubarrayBoundedMax(vector<int>& nums, int left, int right) {
        int n = nums.size();
        int l=-1;
        long long ans=0;
        int r=0;
        int currentInRange=-1;
        while(r<n) {
            if(nums[r]>right) {
                r++;
                l=r-1;
                currentInRange=l;
            } else if(nums[r]>=left && nums[r]<=right) {
                currentInRange=r;
                ans+=r-l;
                r++;
            } else {
                ans+=currentInRange-l;
                r++;
            }
        }
        return ans;
    }
};