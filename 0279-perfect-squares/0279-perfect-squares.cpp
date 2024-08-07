class Solution {
public:

    int f(vector<vector<int>>&dp,vector<int>& sqroot, int index,int sum) {
        if(sum==0) return 0;
        if(index==0) {
            if(sum%sqroot[index]==0) {
                return sum/sqroot[index];
            }
            return 1e7;
        }
        if(dp[index][sum]!=-1) return dp[index][sum];

        return dp[index][sum]=min(
            (sum>=sqroot[index])?1+f(dp,sqroot,index,sum-sqroot[index]):100000,
            f(dp,sqroot,index-1,sum)
            );
        


    }
    int numSquares(int n) {
    vector<vector<int>> dp(3+ceil((double)sqrt(n)),vector<int>(n+1,-1));
    int m=ceil((double)sqrt(n));
    vector<int> sqroot;
    for(int i=1;i<=m;i++) {
        sqroot.push_back(i*i);
    }
    return f(dp,sqroot,sqroot.size()-1,n);
    }
};