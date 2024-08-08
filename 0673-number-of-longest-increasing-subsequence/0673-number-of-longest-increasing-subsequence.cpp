class Solution {
public:

int f(vector<vector<int>>& dp,vector<int>& nums,int prev,int i) {
    if(i==nums.size()) return 0;
    if(dp[i][prev+1]!=-1) return dp[i][prev+1];
    int pick=0;
    int npick=0;
    if(prev==-1 || nums[i]>nums[prev]) {
        pick = 1 + f(dp,nums,i,i+1);
    }
    npick = 0 + f(dp,nums,prev,i+1);
    return dp[i][prev+1] = max(pick,npick);

}
    int findNumberOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> dp(n+1,vector<int>(n+1,-1));
        int maxLengthSol= f(dp,nums,-1,0);

        vector<int> maxLength(n+1,1);
        vector<int> maxLengthCount(n+1,1);
        for(int i=n-2;i>=0;i--) {
            for(int j=i+1;j<n;j++) {
                if(nums[j]>nums[i]&&maxLength[j]>=maxLength[i]) {
                    maxLength[i] = maxLength[j]+1;
                    maxLengthCount[i]=maxLengthCount[j];
                } else if(nums[j]>nums[i]&& maxLength[j]+1==maxLength[i]) {
                    maxLengthCount[i]+=maxLengthCount[j];
                }
            }
        }
        int ans=0;
        for(int i=0;i<n;i++) {
            if(maxLength[i]==maxLengthSol) ans+=maxLengthCount[i];
        }
        return ans;


    }
};