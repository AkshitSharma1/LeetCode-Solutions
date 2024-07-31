class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
     vector<int> copy;
     for(auto num:nums1) copy.push_back(num);
     int i=0;
     int j=0;
     int p=0;
     while(i<m && j<n) {
        if(copy[i]<nums2[j]) {
            nums1[p]=copy[i];
            i++;
        } else {
            nums1[p]=nums2[j];
            j++;
        }
        p++;
     }   
     while(i<m) { nums1[p]=copy[i]; i++; p++;}
     while(j<n) { nums1[p]=nums2[j]; j++;p++;}
    }
};