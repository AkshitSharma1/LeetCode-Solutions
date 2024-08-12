class Solution {
public:
int f(vector<vector<int>>& dp,int l,int r,vector<int>& nums) {
    if(l<0) return 0;
    if(r<l) {cout<<"return 0 as r "<<r<<" and l "<<l<<endl; return 0;}
    if(r>=nums.size()) return 0;
    if(dp[l][r]!=-1) return dp[l][r];
    int ans=INT_MIN;
    int temp_ans=0;
    int prod=0;
    for(int i=l;i<=r;i++) {
        temp_ans = f(dp,l,i-1,nums)+f(dp,i+1,r,nums);
        prod=nums[i];
        if(l-1>=0) prod*=nums[l-1];
        if(r+1<nums.size()) prod*=nums[r+1];
        temp_ans+=prod;
        ans = max(ans,temp_ans);
    }
    return dp[l][r]=ans;

}
    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> dp(n+1,vector<int>(n+1,-1));
        return f(dp,0,n-1,nums);
        
    }
};