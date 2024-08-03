class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int n=nums.size();
        vector<int> minElements(n,INT_MAX);
        minElements[0]=nums[0];
        for(int i=1;i<n;i++) {
            minElements[i] = min(minElements[i-1],nums[i]);
        }
        stack<pair<int,int>> st;
        vector<int> greaterOnLeftIndex(n,-1);
        for(int i=0;i<n;i++) {
            if (st.empty()) {
                st.push({nums[i],i});
            } else {
                while(st.empty()==false && st.top().first<=nums[i]) {
                    st.pop();
                }
                if(st.empty()==false) {
                    greaterOnLeftIndex[i]=st.top().second;
                }
                st.push({nums[i],i});
            }
        }
      
        for(int k=n-1;k>0;k--) {
            if(greaterOnLeftIndex[k]!=-1 && nums[greaterOnLeftIndex[k]]>nums[k]&&nums[greaterOnLeftIndex[k]]>minElements[greaterOnLeftIndex[k]]&&nums[k]>minElements[greaterOnLeftIndex[k]]) return true;
        }
        return false;
    }
};