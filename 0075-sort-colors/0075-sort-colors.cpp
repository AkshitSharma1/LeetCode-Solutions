class Solution {
public:
    void sortArray(vector<int>&nums,int p1,int val) {
        int n = nums.size();
        int p2=1;
        while(p1<n) {
            p2 = p1+1;
            if(nums[p1]!=val) { p1++; continue;}
            if(nums[p1]==val) {
                while(p2<n && nums[p2]==val) p2+=1;
                if(p2==n) break;
                while(p1<n&&p2<n&&nums[p1]==val&&nums[p2]!=val) {
                    swap(nums[p1],nums[p2]);
                    p1+=1;
                    p2+=1;
                }
            }
        }
    }
    void sortColors(vector<int>& nums) {
        sortArray(nums,0,0);
        sortArray(nums,0,1);
        sortArray(nums,0,2);

        
    }
};