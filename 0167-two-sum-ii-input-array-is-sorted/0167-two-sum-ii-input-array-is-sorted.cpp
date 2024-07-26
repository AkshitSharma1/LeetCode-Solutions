class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int n = numbers.size();
        int l = 0;
        int r = n-1;
        int sum=0;
        vector<int> ans(2,-1);
        while(l<r) {
            sum=numbers[l]+numbers[r];
            if (sum==target) {
                ans[0]=l+1;
                ans[1]=r+1;
                return ans;
            } else if(sum>target) {
                r-=1;
            } else {
                l+=1;
            }
        }
        return ans;
        
    }
};