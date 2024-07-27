class Solution {
public:
    int maxArea(vector<int>& height) {
        int l=0;
        int n = height.size();
        int r = n-1;
        int ans=0;
        while(l<r) {
            ans = max(ans,min(height[l],height[r])*(r-l));
            if (height[l]<height[r]) {
                l+=1;
            } else {
                r-=1;
            }

        }
        return ans;
        
    }
};