class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l=0;
        int n = nums.size();
        int r = n-1;
        int index=-1;
        int mid=0;
        while(l<=r) {
            mid = (l+r)/2;
            if (nums[mid]==target) return mid;
            if (nums[l]==target) return l;
            if (nums[r]==target) return r;


                //Search on the smaller half
                if (nums[mid]>nums[l]) {
                    //Left half is sorted
                    if( target<nums[mid]&&target>nums[l]) {
                        //Target lies in this - search it
                        r=mid-1;
                    } else { l = mid+1; } //Search right half
                } else  {
                    //Right half is sorted
                    if(nums[mid]<target&&target<nums[r]) {
                        //Answer lies in this, search it
                        l = mid+1;
                    } else {
                        //Search left half only
                        r=mid-1;
                    }
                }
            }
                        return -1;
    }

    
};