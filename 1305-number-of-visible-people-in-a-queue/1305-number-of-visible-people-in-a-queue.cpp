class Solution {
public:
    vector<int> canSeePersonsCount(vector<int>& heights) {
        stack<int> st;
        int n = heights.size();
        vector<int> ans(n,0);
        int count=0;
        for(int i=n-1;i>=0;i--) {
            count=0;
            if(st.empty()) {
                st.push(heights[i]);
            } else {
                while(st.empty()==false && st.top()<heights[i]) {
                    st.pop();
                    count++;
                }
                if(st.empty()) {ans[i]=count;} else { ans[i]=count+1;}
                st.push(heights[i]);
            }


        }
        return ans;
    }
};