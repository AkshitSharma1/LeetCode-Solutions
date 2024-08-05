class Solution {
public:
    void solve(int n,int unClosedOpenCount, string& temp,vector<string>& results) {
        if(temp.length()==2*n && unClosedOpenCount==0) {
            results.push_back(temp);
            return;
        } else if(temp.length()==2*n) {
            return;
        }

        if(unClosedOpenCount==0) {
            temp+="(";
            solve(n,unClosedOpenCount+1,temp,results);
            temp.pop_back();
        } else {
            temp+="(";
            solve(n,unClosedOpenCount+1,temp,results);
            temp.pop_back();
            temp+=")";
            solve(n,unClosedOpenCount-1,temp,results);
            temp.pop_back();

        }



    }
    vector<string> generateParenthesis(int n) {
        string temp;
        vector<string> results;
        solve(n,0,temp,results);
        return results;
    }
};