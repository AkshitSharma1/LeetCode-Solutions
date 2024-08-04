class Solution {
    void solve(vector<vector<int>> &ans, vector<int> &nums, vector<int> &temp,int index){
        if(temp.size() == nums.size()) {
            ans.push_back(temp); 
            return;
        }
        
        for(int i=index;i<nums.size();i++){
                swap(nums[i],nums[index]);
                temp.push_back(nums[index]);
                solve(ans,nums,temp,index+1);
                swap(nums[i],nums[index]);
                temp.pop_back();
            
        }
        return;
        
    }
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> temp;
        solve(ans,nums,temp,0);
        return ans;
    }
};