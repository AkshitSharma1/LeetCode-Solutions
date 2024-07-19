class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        double ans=1;
        int j=0;
        int i=0;
        int n = nums.size();
        int count=0;
        while(j<n) {
            ans*=nums[j];
            while(i<j && ans>=k) {
                ans/=nums[i];
                i+=1;
            }
                if(ans<k) count+=j-i+1;
                j++;
        }
        return count;
    }
};