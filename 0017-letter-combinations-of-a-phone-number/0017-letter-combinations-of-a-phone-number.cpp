class Solution {
public:

void solve(string& digits,string& temp,vector<string>& results,vector<vector<char>>& mp,int index) {
    if(index==digits.length()) {results.push_back(temp);return; }
    for(auto ch:mp[digits[index]-'0']) {
        temp.push_back(ch);
        solve(digits,temp,results,mp,index+1);
        temp.pop_back();
    }
}
    vector<string> letterCombinations(string digits) {
        
vector<vector<char>> map = {{},{},{'a','b','c'},{'d','e','f'},{'g','h','i'},{'j','k','l'},{'m','n','o'},{'p','q','r','s'},{'t','u','v'},{'w','x','y','z'}};

        string temp;
        vector<string> results;
        if(digits.length()==0)   { return results;}

        solve(digits,temp,results,map,0);
        return results;
    }
};