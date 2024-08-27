class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        int i=0;
        int n = nums.size();
        while(i<n && nums[i]%2==0) i++;
        int j = i+1;
        while(j<n) {
            if(nums[j]%2==0) {
                swap(nums[j],nums[i]);
                i++;
            } 
            j++;
        }
        return nums;
    }
    
};