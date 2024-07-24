class Solution {
public:
    int rangeSum(vector<int>& nums, int n, int left, int right) {
    
        vector<int> prefixSum(n,0);

        prefixSum[0]=nums[0];
        for(int i=1;i<nums.size();i++) {
            prefixSum[i]=prefixSum[i-1]+nums[i];
        }
        vector<long long> possibleSubarraySums;
        for(int i=0;i<n;i++) {
            for(int j=0;j<=i;j++) {
                if(j==0) possibleSubarraySums.push_back(prefixSum[i]);
                if (j>0) possibleSubarraySums.push_back(prefixSum[i]-prefixSum[j-1]);
              //  possibleSubarraySums.push_back(prefixSum[i]-((j>1)?prefixSum[j-1]:0));
            }
        }
        long long MOD = 1e9+7;
        sort(possibleSubarraySums.begin(),possibleSubarraySums.end());

        vector<long long> prefixSum2(possibleSubarraySums.size(),0);
        prefixSum2[0]=possibleSubarraySums[0]%MOD;
        for(int i=1;i<prefixSum2.size();i++) {
            prefixSum2[i]=(prefixSum2[i-1]+possibleSubarraySums[i])%MOD;
            }
        return prefixSum2[right-1]-((left>=2)?prefixSum2[left-2]:0);
        
    }
};