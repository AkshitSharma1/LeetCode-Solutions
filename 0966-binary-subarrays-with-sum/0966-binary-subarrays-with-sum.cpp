class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        //Here neither window size is given (ie. number of subarrays of size k) neither its given to find maximum/min window -> no sliding window
        //But, here we have to find sum of continuous subarrays -> prefix sum
        int n = nums.size();
        vector<int> prefixSum(n,0);
        unordered_map<int,int> mp;
        int ans=0;
        mp[0]=1;
        for(int j=0;j<n;j++) {
            if(j==0) { prefixSum[j] = nums[0]; } else { prefixSum[j] = prefixSum[j-1]+nums[j];}
            int reqSum = prefixSum[j]-goal;
            if(mp.find(reqSum)!=mp.end()) ans+=mp[reqSum];
            mp[prefixSum[j]]++;
        }
        return ans;
        
    }
};