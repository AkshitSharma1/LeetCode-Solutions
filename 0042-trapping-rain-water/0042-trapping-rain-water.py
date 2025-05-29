class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxPrefix = [height[0]]*n
        maxSuffix = [height[-1]]*n
        for i in range(1,n):
            maxPrefix[i] = max(height[i],maxPrefix[i-1])
        
        for i in range(n-2,-1,-1):
            maxSuffix[i] = max(height[i],maxSuffix[i+1])
        

        ans=0
        for i in range(n):
            ans+=max(0,(min(maxPrefix[i],maxSuffix[i])-height[i]))
        
        return ans


        
        