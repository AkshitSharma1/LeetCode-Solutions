class Solution {
public:

    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int,int> mp;
        int i=0;
        int j=0;
        vector<int> prefixSum(nums.size()+1,-1);
        mp[0]=1;
        int ans=0;
        for(int j=0;j<nums.size();j++) {
            if(j==0) {
                prefixSum[j] = nums[0];
            } else {
            prefixSum[j] = prefixSum[j-1]+nums[j];
            }
            int requiredSum = prefixSum[j]-k;

            if(mp.find(requiredSum)!=mp.end()) { ans+=mp[requiredSum];
            }
                        mp[prefixSum[j]]+=1;

        }
        

        

return ans;
        
    }
};