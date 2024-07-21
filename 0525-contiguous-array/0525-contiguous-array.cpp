class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int zeroCount=0;
        int oneCount=0;
        int diff=0;
        unordered_map<int,int> mp; //<diff(one-zero),index of first occurence
        int j=0;
        int ans=0;
        int n=nums.size();
        mp[0]=-1; //Base case so that line 15 executes correctly (giving actual length of subarray)
        while(j<n) {
            if(nums[j]==0) {zeroCount+=1;} else { oneCount+=1;}
            diff = oneCount-zeroCount;
            if(mp.find(diff)!=mp.end()) { ans = max(ans,j-mp[diff]);} else { mp[diff]=j;}
            j+=1;
        }
        return ans;
    }
};