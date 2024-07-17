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
      
        //Window grow phase
        while(j<k) {
            sum+=nums[j];
            mp[nums[j]]+=1;
            if(mp[nums[j]]==2) not_distinct_count+=1;
            j+=1;
        }
        
        if(not_distinct_count==0) max_sum = max(sum,max_sum);
        //Move the above window
        mp[nums[i]]-=1;
        sum-=nums[i];
        if(mp[nums[i]]==1) not_distinct_count-=1;
        i+=1;
     

        
        while(j<n) {
            //Window entering phase
            mp[nums[j]]+=1;
            sum+=nums[j];
            if(mp[nums[j]]==2) {
                //just got repeated
                not_distinct_count+=1;
            }

            //Perform action within window phase
        
            if(not_distinct_count==0) {
                max_sum = max(sum,max_sum);
            }
            //Window moving preparation phase
            sum-=nums[i];
            mp[nums[i]]-=1;
            if(mp[nums[i]]==1) not_distinct_count-=1;
            //Move the window phase
            i++;
            j++;
        }

        
            return max_sum;

    }

};