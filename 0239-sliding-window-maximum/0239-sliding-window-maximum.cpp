class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    int i=0;
    int j=0;
    int n = nums.size();
    vector<int> ans;
    deque<int> dq;
    while(j<k-1) {
        while(!dq.empty() && dq.front()<nums[j]) dq.pop_front();
        dq.push_front(nums[j]);
        j++;
    }
    while(j<n) {
        while(!dq.empty() && dq.front()<nums[j]) dq.pop_front();
        dq.push_front(nums[j]);

        ans.push_back(dq.back());

        if(nums[i]==dq.back()) dq.pop_back();

        i++;
        j++;


    }
    return ans;



    }
};