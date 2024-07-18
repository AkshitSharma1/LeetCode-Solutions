class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        //Consider inverse problem = sum of elements should be exactly x otherwise -1
        //Number of operations = nums.size() - window size to get x as sum
        long long no_sum=0;
        long long total_sum = 0;
        for(auto num:nums) total_sum+=num;
        long long required_sum = total_sum-x;
        int ans=INT_MIN;
       int i=0;
       int j=0;
        int n = nums.size();
        if (total_sum<x) return -1;
        while(j<n) {
            //Act on current window
            no_sum+=nums[j];
            while(no_sum>required_sum) {
                //Shrink the window
                no_sum-=nums[i];
                i++;
            }
            if(no_sum==required_sum) {
                //Here no while sum==x case as no element in nums is 0
                ans = max(ans,(j-i+1));
            }
            //Expand the window to right by 1
            j+=1;
        }
        return ans==INT_MIN?-1:n-ans;
    }
};