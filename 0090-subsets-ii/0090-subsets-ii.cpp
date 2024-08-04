class Solution {
public:
void solve(vector<vector<int>>& results,vector<int>& temp,vector<int>& nums,int index,int n) {
    results.push_back(temp);

    for(int i=index;i<n;i++) {
        if(i!=index && nums[i]==nums[i-1]) continue;
        temp.push_back(nums[i]);
        solve(results,temp,nums,i+1,n);
        temp.pop_back();
    }
}
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
          vector<vector<int>> results;
        vector<int> temp;
        sort(nums.begin(),nums.end());
        solve(results,temp,nums,0,nums.size());
        return results;
    }
};