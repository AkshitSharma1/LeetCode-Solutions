class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int n = nums.size();
        vector<int> minElementToLeft(n,0);
        minElementToLeft[0]=nums[0];
        for(int i=1;i<n;i++) minElementToLeft[i] = min(nums[i],minElementToLeft[i-1]);
        //Stack to find NEXT GREATER ELEMENT TO LEFT
        stack<pair<int,int>> st;
        vector<int> NGLIndex(n,-1);
        for(int i=0;i<n;i++) {
            if(st.empty()) {
                st.push({nums[i],i});
            } else {
                while(!st.empty() && st.top().first<=nums[i]) {
                    st.pop();
                }
                if(!st.empty()) {
                    NGLIndex[i] = st.top().second;
                    
                } 
                st.push({nums[i],i});

            }
        }
        for(int k=n-1;k>0;k--) {
            int j = NGLIndex[k];
            if(j==0 || j==-1) continue;
            if(minElementToLeft[j-1]<nums[k]) return true;
        }
        return false;
    }
};