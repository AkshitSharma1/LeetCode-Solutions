class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> ans(n,0);
        stack<pair<int,int>> st;
        for(int i=n-1;i>=0;i--) {
            if(st.empty()) {
                st.push({temperatures[i],i});
            } else {
                while(st.empty()==false && st.top().first<=temperatures[i]) {st.pop();}
                if(st.empty()==false) {
                    ans[i] = st.top().second;}
                st.push({temperatures[i],i});
            }
        }
        for(int i=n-1;i>=0;i--) {
            if(ans[i]==0) continue;
            ans[i] = ans[i]-i;
        }
        return ans;
    }
};