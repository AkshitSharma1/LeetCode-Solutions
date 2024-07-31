class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int l=1;
        int r=1;
        int prevCount=0;
        int n = nums.size();
        while(r<n) {
            if(nums[r]==nums[r-1]) {
                if(prevCount==0) {
                    nums[l]=nums[r];
                    l++;
                    r++;
                } else {
                    r++;
                }
                prevCount+=1;
            } else {
                nums[l]=nums[r];
                l++;
                r++;
                prevCount=0;
            }
        }
        return l;
        
    }
};