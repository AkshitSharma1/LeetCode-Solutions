class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& nums) {
        int p1=0;
        int p2=1;
        int n = nums.size();
        while(p1<n) {
            p2=p1+1;
            if((p1%2==0 && nums[p1]%2==0) || (p1%2==1 && nums[p1]%2==1)) { p1++; continue;}
            if((p1%2==0&&nums[p1]%2==1)||(p1%2==1 && nums[p1]%2==0)) {
                //Move p2 till we find some suitable place for swapping
                while(p2<n && p1%2!=nums[p2]%2) p2++;
                if (p2==n) break;
                swap(nums[p1],nums[p2]);
                p1++;
                p2++;
            }
        }
        return nums;
        
    }
};