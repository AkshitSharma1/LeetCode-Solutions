class Solution {
public:
    void solve(vector<int>& nums,unordered_map<int,int>&mp, vector<int>& temp,vector<vector<int>>& results) {

        if(temp.size()==nums.size()){ results.push_back(temp); return; }
        for(auto& pair:mp) {
            if(pair.second==0) continue;
            pair.second-=1;
            temp.push_back(pair.first);
            solve(nums,mp,temp,results);
            temp.pop_back();
            pair.second+=1;
        }
    }
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        unordered_map<int,int> mp;
        for(auto num:nums) mp[num]++;
        vector<int> temp;
        vector<vector<int>> results;
        solve(nums,mp,temp,results);
        return results;
        
    }
};