class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        int n = nums.size();
        int i=0;
        int j=0;
        long long max_sum=0;
        long long sum=0;
        long long not_distinct_count=0;
        unordered_map<int,int> mp;

        while(j<k-1) {
            //Window grow phase
            if(++mp[nums[j]]==2) not_distinct_count+=1;
            sum+=nums[j];
            j+=1;
        }
       
        while(j<n) {
            //Window entering phase
            if(++mp[nums[j]]==2) not_distinct_count+=1;
            sum+=nums[j];

            //Window process phase
            if(not_distinct_count==0) max_sum = max(sum,max_sum);

            //Window prepare to move phase 
            if(--mp[nums[i]]==1) not_distinct_count-=1;
            sum-=nums[i];
            

            //Move window phase
            i+=1;
            j+=1;
        }

        return max_sum;


    }
};