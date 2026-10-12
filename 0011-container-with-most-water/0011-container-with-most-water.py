class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        n = len(height)
        r = n-1
        max_area = 0
        area = 0
        while l<r:
            area = min(height[r],height[l])*(r-l)
            max_area = max(max_area,area)
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return max_area
        


        