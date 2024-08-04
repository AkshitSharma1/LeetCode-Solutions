class Solution {
public:
    void solve(vector<vector<int>>& results,vector<int>& temp,vector<int>& nums,int index) {
        if(index==nums.size()) return;
        //First try selecting element
        temp.push_back(nums[index]);
        //Now push this into results
        results.push_back(temp);
        //Recurse
        solve(results,temp,nums,index+1);
        //Backtrack
        temp.pop_back();
        //What if we dont select?
        solve(results,temp,nums,index+1);

    }
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> results;
        vector<int> temp;
        results.push_back(temp);
        solve(results,temp,nums,0);
        return results;

        
    }
};