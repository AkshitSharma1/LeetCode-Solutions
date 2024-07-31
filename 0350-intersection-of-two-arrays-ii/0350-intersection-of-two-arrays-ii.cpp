class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int,int> mp1,mp2;
        int n=nums1.size();
        int m=nums2.size();
        for(auto num1:nums1) mp1[num1]++;
        for(auto num2:nums2) mp2[num2]++;
        vector<int> ans;
        for(auto num1:nums1) {
            if(mp2.find(num1)!=mp2.end() && mp2[num1]!=0) {
              int  minCommonCount = min(mp1[num1],mp2[num1]);
              mp1[num1]=0;
              mp2[num1]=0;
            while(minCommonCount--!=0) ans.push_back(num1);
            }
        }
        return ans;


        
    }
};