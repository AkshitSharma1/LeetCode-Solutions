class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        sort(nums1.begin(),nums1.end());
        sort(nums2.begin(),nums2.end());
        int n=nums1.size();
        int m = nums2.size();
        int i=0;
        vector<int> ans;
        while(i<n) {
            if(i!=0 && nums1[i]==nums1[i-1]) {i++; continue;}
            auto lowerBound = lower_bound(nums2.begin(),nums2.end(),nums1[i]);
            if(lowerBound!=nums2.end() && *lowerBound==nums1[i])  {
                ans.push_back(nums1[i]);
            }
            i++;

        }
        return ans;

            }
};