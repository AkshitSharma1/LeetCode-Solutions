class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        nsr_stack,nsl_stack = [],[]
        n = len(heights)

        nsr,nsl = [n]*n,[-1]*n
        for i in range(n-1,-1,-1):
            while nsr_stack and heights[nsr_stack[-1]]>=heights[i]:
                nsr_stack.pop()
            if nsr_stack: nsr[i] = nsr_stack[-1]
            nsr_stack.append(i)
        for i in range(0,n,1):
            while nsl_stack and heights[nsl_stack[-1]]>=heights[i]:
                nsl_stack.pop()
            if nsl_stack: nsl[i] = nsl_stack[-1]
            nsl_stack.append(i)
        answer = 0
        for i in range(n):
            answer = max(answer,(nsr[i]-nsl[i]-1)*heights[i])
        return answer
        