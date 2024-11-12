class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> dq;
        int r=0;
        vector<int> ans;
        while(r<k) {
            if(dq.empty()) {
                dq.push_front(nums[r]);
            
            } else {
                while (!dq.empty() && dq.front()<nums[r]) {
                dq.pop_front();
            }
            dq.push_front(nums[r]);
            }
            r+=1;
        }
        int l=0;
        ans.push_back(dq.back());
        if(nums[l]==dq.back()) {
            dq.pop_back();
        }
        l+=1;
        while(r<nums.size()) {
                if(dq.empty()) {
                dq.push_front(nums[r]);
            
            } else {
                while (!dq.empty() && dq.front()<nums[r]) {
                dq.pop_front();
            }
            dq.push_front(nums[r]);
            }

        ans.push_back(dq.back());




            //Move both forward
            r+=1;
            if (dq.back()==nums[l]) { dq.pop_back(); }
            l+=1;
        }
        return ans;
    }
};