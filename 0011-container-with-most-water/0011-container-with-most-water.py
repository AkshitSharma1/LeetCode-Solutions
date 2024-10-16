class Solution:
    def maxArea(self, height: List[int]) -> int:
        lIndex=0
        rIndex = len(height)-1
        ans=0
        while lIndex<rIndex:
            ans = max(ans,min(height[lIndex],height[rIndex])*(rIndex-lIndex))
            if height[lIndex]<height[rIndex]:
                 lIndex+=1
            else: rIndex-=1
        return ans
        