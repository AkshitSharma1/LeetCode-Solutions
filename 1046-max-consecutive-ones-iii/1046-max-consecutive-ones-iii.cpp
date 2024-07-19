class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        //We can flip at most k nums 
        int i=0;
        int j=0;
        int ans=0;
        int flip_count=0;
        int n = nums.size();
        while(j<n) {
            if (nums[j]==0)  flip_count+=1;
            while(flip_count>k) {
                if(nums[i]==0) flip_count-=1;
                i++;
            }

            if(flip_count<=k) ans = max(ans,j-i+1);
            j++;
        }
        return ans;
        
    }
};