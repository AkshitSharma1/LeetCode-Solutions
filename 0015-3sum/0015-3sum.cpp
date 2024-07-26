class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        set<vector<int>> uniqueElements;
        int n = nums.size();
        int target=0;
        int i=0;
        int sum=0;
        int j;
        vector<vector<int>> ans;
        for(int start=0;start<n;start++) {
            target=(-1)*nums[start];
            //Two pointer
            i = start+1;
            j = n-1;
            if(i>=n || j<0) break;
            while(i<j) {
                sum = nums[i]+nums[j];
                if(sum==target) {
                    uniqueElements.insert({nums[start],nums[i],nums[j]});
                    i+=1;
                }  else if(sum>target) {
                    j-=1;
                } else {
                    i+=1;
                }
            }
            
            
        }
        for(auto uniqueElement:uniqueElements) ans.push_back(uniqueElement);
        return ans;

    }
};