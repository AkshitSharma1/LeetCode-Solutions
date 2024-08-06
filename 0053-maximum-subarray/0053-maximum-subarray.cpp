class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        long long i=0;
        long long currSum=0;
        long long maxSum=INT_MIN;
        for(auto num:nums) {
            currSum+=num;
             maxSum = max(currSum,maxSum);

            if(currSum<0) {
                currSum=0;
                continue;
            }
        }
        return  maxSum;
        
    }
};