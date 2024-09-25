class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        leftMax = [height[_] for _ in range(n)]
        rightMax = [height[_] for _ in range(n)]
        ans=0
        
        
        for i in range(1,n):
            leftMax[i] = max(height[i],leftMax[i-1])
        for i in range(n-2,-1,-1):
            rightMax[i] = max(height[i],rightMax[i+1])
        
     
        
        for i in range(n):
            ans+=min(leftMax[i],rightMax[i])-height[i]
        return ans



        