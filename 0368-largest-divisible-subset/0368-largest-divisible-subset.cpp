class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        int n = nums.size();
        sort(nums.begin(),nums.end());
        vector<int> dp(n+1,1);
        vector<int> pointer(n+1,1);
        for(int i=0;i<=n;i++) pointer[i]=i;
        for(int i=n-1;i>=0;i--) {
            for(int j=i+1;j<n;j++) {
                if (nums[j]>nums[i]&&(nums[j]%nums[i]==0 || nums[i]%nums[j]==0) && dp[j]+1>dp[i]) {
                    dp[i] = max(dp[i],dp[j]+1);
                    pointer[i]=j;
                }
            }
        }
        int maxElementPointer = max_element(dp.begin(),dp.end())-dp.begin();
        vector<int> ans;
        while(pointer[maxElementPointer]!=maxElementPointer) {
            ans.push_back(nums[maxElementPointer]);
            maxElementPointer=pointer[maxElementPointer];
            
        }
                    ans.push_back(nums[maxElementPointer]);

        
        return ans;
    }
};