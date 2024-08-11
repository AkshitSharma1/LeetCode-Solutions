class Solution {
public:

    bool f(vector<vector<int>>& dp,vector<string>& words,unordered_set<string>& wrds, int index,int l,int r) {
       
       if(l>r || l>=r) return true;
        if(dp[index][l]!=-1) return dp[index][l];
        for(int i=l;i<r;i++) {
         
            bool status = f(dp,words,wrds,index,i+1,r);
            if(wrds.find(words[index].substr(l,i-l+1))!=wrds.end()&&*wrds.find(words[index].substr(l,i-l+1))!=words[index]&& status) {
                return dp[index][l]=true;
                
            }
        }
        return dp[index][l]=false;

    }
    vector<string> findAllConcatenatedWordsInADict(vector<string>& words) {
        unordered_set<string> wrds;
        vector<string> ans;
    for(string word : words) {
        wrds.insert(word);
    }  
          vector<vector<int>> dp(words.size()+1,vector<int>(31,-1));
        for(int i=0;i<words.size();i++) {
            if(f(dp,words,wrds,i,0,words[i].size())) ans.push_back(words[i]);
        }
        return ans;
    }
};