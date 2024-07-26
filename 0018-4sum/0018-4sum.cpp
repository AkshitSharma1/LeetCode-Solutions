class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        long long l=0;
        long long r=0;
        long long n = nums.size();
        long long sum=0;
        vector<vector<int>> ans;
        for(long long start1=0;start1<n;start1++) {
            if(start1>=1 && nums[start1-1]==nums[start1]) continue;

            for(long long start2=start1+1;start2<n;start2++) {
                if(start2-start1>=2 && nums[start2-1]==nums[start2]) continue;
                l=start2+1;
                r = n-1;
                while(l<r) {
                    if (l>=n) break;
                    sum= nums[start1];
                    sum+=nums[start2];
                    sum+=nums[l];
                    sum+=nums[r];
                    if(sum==target) {
                        ans.push_back({nums[start1],nums[start2],nums[l],nums[r]});
                        l+=1;
                        while(l<n&& nums[l]==nums[l-1]) l+=1;
                    } else if(sum>target) {
                        r-=1;
                    } else {
                        l+=1;
                    }
                }
            }
        }
        return ans;
    }
};