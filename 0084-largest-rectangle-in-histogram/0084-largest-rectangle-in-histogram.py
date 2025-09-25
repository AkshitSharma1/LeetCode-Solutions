class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        NSR,NSL = [n]*n,[-1]*n
        NSRStack,NSLStack = [],[]
        for i in range(n-1,-1,-1):
            while NSRStack and heights[NSRStack[-1]]>=heights[i]:
                NSRStack.pop()
            if NSRStack:
                NSR[i] = NSRStack[-1]
            NSRStack.append(i)
        
        for i in range(0,n,1):
            while NSLStack and heights[NSLStack[-1]]>=heights[i]:
                NSLStack.pop()
            if NSLStack:
                NSL[i] = NSLStack[-1]
            NSLStack.append(i)
        
        maxArea = 0
        for i in range(n):
            maxArea = max(maxArea,(NSR[i]-NSL[i]-1)*heights[i])
        return maxArea
        


        