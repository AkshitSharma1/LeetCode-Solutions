class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        //O(nlgn)
        vector<int> copy;
        for(auto num:nums) copy.push_back(num);
        sort(copy.begin(),copy.end());
        int minIndex=-1;
        int maxIndex=-1;
        for(int i=0;i<copy.size();i++) {
            if(copy[i]!=nums[i]) {
               if(minIndex==-1) minIndex=i;
                maxIndex=i;
            }
        }
        if(minIndex!=-1) {
        return maxIndex-minIndex+1;
        }
        return 0;
    }
};