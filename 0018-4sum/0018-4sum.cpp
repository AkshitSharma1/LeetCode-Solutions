class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        long long goal = 0;
        vector<vector<int>> ans;
        int n = nums.size();
        sort(nums.begin(),nums.end());
        for(int i=0;i<n;i++) {
            if (i>0 && nums[i]==nums[i-1]) continue;
            goal =nums[i];
            for(int j=i+1;j<n;j++) {
                if(j>i+1 && nums[j]==nums[j-1]) continue;
                goal=nums[i]+nums[j];
                int start=j+1;
                int end=n-1;
                while(start<end) {
                    if(start>j+1 && nums[start]==nums[start-1]) { start++; continue;}
                    if(goal+nums[start]+nums[end]==target) {
                        ans.push_back({nums[i],nums[j],nums[start],nums[end]});
                        start++;
                        while(start<n && nums[start]==nums[start-1]) { start++;}
                    } else if(goal+nums[start]+nums[end]>target) {end--;} else { start++;}
                }

            }
        }
    return ans;
    }
};