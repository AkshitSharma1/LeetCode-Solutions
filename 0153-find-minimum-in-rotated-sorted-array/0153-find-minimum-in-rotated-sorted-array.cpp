class Solution {
public:
    int findMin(vector<int>& nums) {
      int l=0;
      int r = nums.size()-1;
      int mid = (l+r)/2;
      int ans=INT_MAX;
      while(l<=r) {
        mid = (l+r)/2;
        ans = min(ans,nums[mid]);
        if (nums[l]<=nums[r]) return nums[l];
        if (nums[l]<=nums[mid]) {
            //By visualization, ssearch right half
            l = mid+1; 
        } else {
            //Right portion is sorted -> search the half
            r = mid;

        }
      }
      return ans;
    }
};