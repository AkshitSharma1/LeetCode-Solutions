class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        int prefixSum=0;
        unordered_map<int,int> mp;
        mp[0]=1;
        int ans=0;
        for(auto num:nums) {
            num%=k;
            if(num<0) num+=k;
            prefixSum+=num;
            prefixSum%=k;
            int diff=(prefixSum-k)%k;
            if(diff<0) diff+=k;
            if(mp.find(diff)!=mp.end()) ans+=mp[diff];
            mp[prefixSum]+=1;
            
        }
        return ans;
    }

};