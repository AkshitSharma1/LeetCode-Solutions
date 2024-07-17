class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int i=0;
        int j=0;
        int n = nums.size();
        double avg=INT_MIN;
        double movingSum=0;
        //Window grow phase
        while(j<k-1) {
            movingSum+=nums[j];
            j=j+1;
        }

        while(j<n) {
            //Process the window phase
            movingSum+=nums[j];
            avg=max(movingSum/k,avg);
            //Prepare to move the window phase
            movingSum-=nums[i];
            //Move the window phase
            i++;
            j++;
        }
            return avg;

    }
};