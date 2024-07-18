class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int i=0;
        int j=0;
        int n = nums.size();
        int nice_count=0;
        int odd_count=0;
        while(j<n) {
            odd_count+=nums[j]%2;
           
            while(odd_count>k) {
                odd_count-=nums[i]%2;
                i++;
            }

            if(odd_count==k) {
                int temp = i;
                while(temp<j && nums[temp]%2==0) {
                    temp++;
                }
                nice_count += temp - i + 1;
            }
            j++;
        }
        return nice_count;
    }
};
