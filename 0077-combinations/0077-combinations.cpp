class Solution {
public:
    void solve(vector<int>& temp,vector<vector<int>>& result,int n,int k,int index) {
        if(temp.size()==k) {
            result.push_back(temp);
            return;
        }
        for(int i=index;i<=n;i++) {
            temp.push_back(i);
            solve(temp,result,n,k,i+1);
            temp.pop_back();
        }
    }
    vector<vector<int>> combine(int n, int k) {
        vector<int> nums,temp;
        vector<vector<int>> result;
        solve(temp,result,n,k,1);
        return result;
    }
};