class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        NSR = [n]*n
        NSL = [-1]*n
        stack = []
        for i in range(n-1,-1,-1):
            while len(stack)>0 and heights[i]<=heights[stack[-1]]:
                stack.pop()

            if len(stack)>0:
                NSR[i] = stack[-1]
            
            stack.append(i)

        stack = []
        for i in range(0,n,+1):
            while len(stack)>0 and heights[i]<=heights[stack[-1]]:
                stack.pop()

            if len(stack)>0:
                NSL[i] = stack[-1]
            
            stack.append(i)
        answer = 0
        for index,histogramHeight in enumerate(heights):
            answer = max(answer,
            (NSR[index]-NSL[index]-1)*histogramHeight
            
            )
        return answer

            

        