class Solution:
    def trap(self, height: list[int]) -> int:
        l = 0
        r = len(height)-1
        max_height_l,max_height_r = 0,0
        ans = 0
        while l<=r:
            max_height_l = max(max_height_l,height[l])
            max_height_r = max(max_height_r,height[r])
            if max_height_l<=max_height_r:
                ans += max_height_l-height[l]
                l+=1
            else:
                ans+=max_height_r-height[r]
                r-=1
        return ans


            
        