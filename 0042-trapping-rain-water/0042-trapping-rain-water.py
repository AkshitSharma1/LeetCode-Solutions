class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        left_max_height = height[0]
        right_max_height = height[n-1]
        ans = 0
        while l<=r:
            left_max_height = max(left_max_height,height[l])
            right_max_height = max(right_max_height,height[r])

            if left_max_height<right_max_height:
                ans+=max(0,
                left_max_height-height[l])
                l+=1
            else:
                ans+=max(0,
                right_max_height-height[r])
                r-=1
        return ans


