class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        NSLStack,NSRStack = [],[]
        n = len(heights)
        NSL = [-1]*n
        NSR = [n]*n

        #First we calculate NSR
        for i in range(n-1,-1,-1):
            while len(NSRStack)>0 and heights[NSRStack[-1]]>=heights[i]:
                NSRStack.pop()
            if len(NSRStack)>0:
                NSR[i] = NSRStack[-1]
            NSRStack.append(i)
        for i in range(0,n,1):
            while len(NSLStack)>0 and heights[NSLStack[-1]]>=heights[i]: NSLStack.pop()
            if len(NSLStack)>0: NSL[i]  = NSLStack[-1]
            NSLStack.append(i)
        maxAnswer = 0
        for i,height in enumerate(heights):
            maxAnswer = max(maxAnswer,height*(NSR[i]-NSL[i]-1))
        return maxAnswer
        