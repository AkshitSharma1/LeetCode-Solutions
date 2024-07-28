class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int n =nums.size();
        vector<int> ans;
        int minElement=INT_MAX;
        int minIndex=0;
        for(int i=0;i<n;i++) {
            nums[i] = abs(nums[i]);
            if(nums[i]<minElement) {
                minElement = nums[i];
                minIndex=i;
            }
        }
        int lPointer=minIndex-1;
        int rPointer=minIndex+1;
        ans.push_back(minElement*minElement);
        while(lPointer>=0&&rPointer<n) {
            if(nums[lPointer]==nums[rPointer]) {
                ans.push_back(nums[lPointer]*nums[lPointer]);
                ans.push_back(nums[rPointer]*nums[rPointer]);
                lPointer-=1;
                rPointer+=1;

            } else if(nums[lPointer]<nums[rPointer]) {
                ans.push_back(nums[lPointer]*nums[lPointer]);
                lPointer-=1;
            } else if(nums[lPointer]>nums[rPointer]) {
                ans.push_back(nums[rPointer]*nums[rPointer]);
                rPointer+=1;
            }
        }
        while(lPointer>=0) {ans.push_back(nums[lPointer]*nums[lPointer]); lPointer-=1;}
        while(rPointer<n) {ans.push_back(nums[rPointer]*nums[rPointer]); rPointer+=1;}
    return ans;
    }
};