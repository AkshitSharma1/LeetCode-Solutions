class Solution {
public:
    int numSubarrayBoundedMax(vector<int>& nums, int left, int right) {
        stack<pair<int,int>> NGLStack;
        stack<pair<int,int>> NGRStack;
        int n = nums.size();
        vector<int> NGL(n,-1);
        vector<int> NGR(n,n);
        for(int i=0;i<n;i++) {
            if(!NGLStack.empty()) {
                while(!NGLStack.empty()&&NGLStack.top().first<nums[i]) {
                    NGLStack.pop();
                }
                if(!NGLStack.empty()) {
                    NGL[i] = NGLStack.top().second;
                }
            }
            NGLStack.push({nums[i],i});
        }


          for(int i=n-1;i>=0;i--) {
            if(!NGRStack.empty()) {
                while(!NGRStack.empty()&&NGRStack.top().first<=nums[i]) {
                    NGRStack.pop();
                }
                if(!NGRStack.empty()) {
                    NGR[i] = NGRStack.top().second;
                }
            }
            NGRStack.push({nums[i],i});
        }
        int ans=0;
        for(int i=0;i<n;i++) {
            if(!(nums[i]<=right && nums[i]>=left)) continue;
            cout<<i<<endl;
            ans+=(NGR[i]-i)*(i-NGL[i]);
        }
        return ans;
    }
};