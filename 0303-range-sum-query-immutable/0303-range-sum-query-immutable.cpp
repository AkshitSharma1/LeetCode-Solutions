class NumArray {
public:
        vector<int> prefixSum;

    NumArray(vector<int>& nums) {
        prefixSum.resize(nums.size());
      
        for(int i=0;i<nums.size();i++) {
            if (i==0) {
                prefixSum[i] = nums[i];
            } else {
                prefixSum[i] = prefixSum[i-1]+nums[i];
            }
        }
        
        
    }
    
    int sumRange(int left, int right) {
        if(left==0) {
            return prefixSum[right];
        } else {
            return prefixSum[right]-prefixSum[left-1];
        }
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */