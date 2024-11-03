class Solution {
public:
    void sortColors(vector<int>& nums) {
        int i=0;
        while(i<nums.size() && nums[i]==0) i+=1;
        int j=i+1;
        //First bring 0 together
        while(j<nums.size()) {
             while( i<nums.size() && nums[i]==0) {
                    i++;
                    j++;
                }
                if(j>=nums.size()) break;
            if(nums[j]==0) {
                swap(nums[i],nums[j]);
                i+=1;
                j+=1;
               
            } else {
                j+=1;
            }
        }
        
        j=i+1;
        while(j<nums.size()) {
             while( i<nums.size() && nums[i]==1) {
                    i++;
                    j++;
                }
                if(j>=nums.size()) break;
            if(nums[j]==1) {
                swap(nums[i],nums[j]);
                i+=1;
                j+=1;
               
            } else {
                j+=1;
            }
        }
       
    }
};