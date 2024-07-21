class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> prefixSum(n+1,0);
        unordered_map<int,int> mp;
        int ans=0;
        //Initialize base case - when sum of elements is exactly =k, 
        //We can also pick subarray such that sum[0,j] =k and no smaller  subarray within [0,j] has sum=k
        mp[0]=1;
        for(int j=0;j<n;j++) {
            //Calculate prefix sum 
            if(j==0) { prefixSum[0] = nums[0];} else { prefixSum[j] = prefixSum[j-1]+nums[j];}
            int requiredSum = prefixSum[j]-k;
            if(mp.find(requiredSum)!=mp.end()) ans+=mp[requiredSum]; 
            //Say prefix sum at j= 50, k=30 we can form number of subarrays using prefix sum =20 encountered so far
            mp[prefixSum[j]]+=1;


        }
        return ans;
    }
};