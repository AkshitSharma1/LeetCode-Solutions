class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
          int n = nums.size();
        int p2=1;
        int p1=0;
        while(p1<n) {
            p2 = p1+1;
            if(nums[p1]%2==0) { p1++; continue;}
            if(nums[p1]%2==1) {
                while(p2<n && nums[p2]%2==1) p2+=1;
                if(p2==n) break;
                while(p1<n&&p2<n&&nums[p1]%2==1&&nums[p2]%2==0) {
                    swap(nums[p1],nums[p2]);
                    p1+=1;
                    p2+=1;
                }
            }
        }
        return nums;
    }

};