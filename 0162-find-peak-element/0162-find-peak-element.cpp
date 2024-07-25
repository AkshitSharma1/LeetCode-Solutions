class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int l=0;
        int r = nums.size()-1;
        if (nums.size()==1) return 0;
        int mid=0;
        while(l<=r) {
            mid = (l+r)/2;
            if (mid>0 && mid<nums.size()-1 ) {
                if(nums[mid]>nums[mid-1]&&nums[mid]>nums[mid+1]) {
                    return mid;
                } else if(nums[mid]<=nums[mid+1]&&nums[mid-1]<=nums[mid]) {
                    //pick must occur on right
                    l = mid+1;
                } else if(nums[mid-1]>=nums[mid] && nums[mid]>=nums[mid+1]) {
                    //pick must occur on left
                    r = mid-1;
                } else {
                    r=mid-1;
                }
            } else {
                cout<<mid<<endl;
                if(mid==nums.size()-1) {
                    if(nums[mid]>=nums[mid-1]) {return mid; } else { return mid-1; }
                } else if(mid==0) {
                    if (nums[mid]>=nums[mid+1])  {return mid; } else { return mid+1; }
                }
            }

        }
        return 1;
    }
};