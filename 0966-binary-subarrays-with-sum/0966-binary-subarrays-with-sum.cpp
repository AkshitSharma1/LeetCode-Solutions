class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        unordered_map<int,int> mp; //prefixsum,count
        mp[0]=1;
        int prefixSum=0;
        int ans=0;
        for(auto num:nums) {
            prefixSum+=num;
            int diff = prefixSum-goal;
            if(mp.find(diff)!=mp.end()) ans+=mp[diff];
            mp[prefixSum]++;
        }
         return ans;

    }
};