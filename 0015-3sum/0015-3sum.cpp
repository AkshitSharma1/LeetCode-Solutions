class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
  
        int n = nums.size();
        int target=0;
        int i=0;
        int sum=0;
        int j;
        vector<vector<int>> ans;
        for(int start=0;start<n;start++) {
            if (start>0 && nums[start]==nums[start-1]) continue;
            target=(-1)*nums[start];
            //Two pointer
            i = start+1;
            j = n-1;
            while(i<j) {
                if(i>=n || j<0) break;

                sum = nums[i]+nums[j];
                if(sum==target) {
                    ans.push_back({nums[start],nums[i],nums[j]});
                    i+=1;
                    while (i<n && nums[i]==nums[i-1]) i+=1;
                }  else if(sum>target) {
                    j-=1;
                } else {
                    i+=1;
                }
            }
            
            
        }
        return ans;

    }
};