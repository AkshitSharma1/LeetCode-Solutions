class Solution {
public:
    void solve(int index, vector<int>& nums,vector<int>& temp,vector<vector<int>>& finalAns) {
        if (index==nums.size()) {
            finalAns.push_back(temp);
            return;
        }
        //For index position, try all possible options
        for (int i=0;i<nums.size();i++) {
            if (nums[i]!=11) {
                int tempVar = nums[i];
                temp.push_back(nums[i]);
                nums[i]=11;

                solve(index+1,nums,temp,finalAns);
                temp.pop_back();
                nums[i] = tempVar;
            }
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> finalAns;
        vector<int> temp;
         solve(0,nums,temp,finalAns);
         return finalAns;
        
        
    }
};