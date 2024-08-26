class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int sum=0;
        int n = nums.size();
        vector<vector<int>> ans;

        for(int start=0;start<n;start++) {
            if(start>0 && nums[start]==nums[start-1]) { continue;}
            sum=nums[start];
            int i = start+1;
            int j = n-1;
            while(i<n && j>0 && i<j ) {
               // if(i>start+1 && nums[i]==nums[i-1]) { i++; continue;}
                if(sum+nums[i]+nums[j]==0) {
                    ans.push_back({nums[start],nums[i],nums[j]});
                    i++;
                    while(i<n && nums[i]==nums[i-1]) i++;
                } else if(sum+nums[i]+nums[j]>0) {
                    //We want to decrease sum
                    //Move j left
                    j-=1;
                } else {
                    i+=1;
                }
            }

        }
        return ans;
    }
};