class Solution {
public:
void solve(vector<int>& temp,vector<vector<int>>& results,vector<int>& candidates,int index,int target,int n) {
    if(target==0) {
        results.push_back(temp);
        return;
    }
    for(int i=index;i<n;i++) {
         if(i!=index && candidates[i]==candidates[i-1]) {
                //Remove the duplicate combination case
                continue;
            }
        if(target-candidates[i]>=0) {
           
            temp.push_back(candidates[i]);
            solve(temp,results,candidates,i+1,target-candidates[i],n);
            temp.pop_back();
        }
    }
    
    
}
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> results;
        vector<int> temp;
        sort(candidates.begin(),candidates.end());
        solve(temp,results,candidates,0,target,candidates.size());
        return results;

    }
};