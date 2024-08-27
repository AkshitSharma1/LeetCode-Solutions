class Solution {
public:
    void sortiT(vector<int>& nums,int oldColor,int newColor) {
      int i=0;
      while((i<nums.size() && nums[i]==newColor) || oldColor!=-1 && i<nums.size()&&nums[i]!=oldColor) i++;
      int j=i+1;
      while(j<nums.size()) {
         if(oldColor!=-1 && i<nums.size()&&nums[i]!=oldColor)  {i++; j=i+1; continue; }

        if(nums[j]==newColor) { 
            swap(nums[j],nums[i]);
            j++;
            i++;
        } else {
            j++;
        }
        
      }
    }
    void sortColors(vector<int>& nums) {
        sortiT(nums,-1,0);
        sortiT(nums,2,1);
      //  return nums;
    }
};