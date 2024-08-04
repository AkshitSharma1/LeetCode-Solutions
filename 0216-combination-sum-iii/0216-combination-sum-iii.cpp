class Solution {
public:
void solve(vector<int>& temp,vector<vector<int>>& results,vector<int>& candidates,int index,int target,int n,int k) {
    if(target==0 && temp.size()==k) {
        results.push_back(temp);
        return;
    } else if(target==0) { return; }
    for(int i=index;i<n;i++) {
         if(i!=index && candidates[i]==candidates[i-1]) {
                //Remove the duplicate combination case
                continue;
            }
        if(target-candidates[i]>=0) {
           
            temp.push_back(candidates[i]);
            solve(temp,results,candidates,i+1,target-candidates[i],n,k);
            temp.pop_back();
        }
    }
    
    
}
    vector<vector<int>> combinationSum3(int k,int n) {
        vector<vector<int>> results;
        vector<int> temp;
        vector<int> candidates;
        for(int i=1;i<=9;i++) candidates.push_back(i);
        solve(temp,results,candidates,0,n,candidates.size(),k);
        return results;

    }
};