class Solution {
public:
    int numOfSubarrays(vector<int>& nums, int k, int threshold) {
      int i=0;
        int j=0;
        int n = nums.size();
        int count=0;
        double movingSum=0;
        //Window grow phase
        while(j<k- 1) {
            movingSum+=nums[j];
            j=j+1;
        }

        while(j<n) {
            //Process the window phase
            movingSum+=nums[j];
            if(movingSum/k>=threshold) count++;
            //Prepare to move the window phase
            movingSum-=nums[i];
            //Move the window phase
            i++;
            j++;
        }
            return count;

    }  
    
};