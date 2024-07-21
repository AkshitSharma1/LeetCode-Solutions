class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        long long n = nums.size();
        vector<long long> prefixSum(n,0);
        long long j=0;
        unordered_map<long long,long long> mp;
        mp[0]=-1;
        while(j<n) {
            if(j==0) { prefixSum[0]=nums[0];} else {prefixSum[j]=prefixSum[j-1]+nums[j]; }
            prefixSum[j]%=k;
            if(mp.find(prefixSum[j])!=mp.end()&&j-mp[prefixSum[j]]>=2) return true;
            if(mp.find(prefixSum[j])==mp.end()) mp[prefixSum[j]]=j;
            j++;
        }
        return false;
    }
};