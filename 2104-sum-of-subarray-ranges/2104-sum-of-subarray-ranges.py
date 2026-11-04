class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        #NBR,NBL,NSL,NSR
        NBL_stack = []
        NBR_stack = []
        n = len(nums)
        NBL = [-1]*n
        NBR = [n]*n
        NSL = [-1]*n
        NSR = [n]*n
        NSL_stack = []
        NSR_stack = []

        #first do NBR, NBL for max value
        #mootonic decreasng stack
        #NBR 
        for i in range(n-1,-1,-1):
            while NBR_stack and nums[NBR_stack[-1]]<nums[i]:
                NBR_stack.pop()
            
            if NBR_stack: NBR[i] = NBR_stack[-1]
            NBR_stack.append(i)
        
        #NBL
        for i in range(0,n):
            while NBL_stack and nums[NBL_stack[-1]]<=nums[i]:
                NBL_stack.pop()
            
            if NBL_stack: NBL[i] = NBL_stack[-1]
            NBL_stack.append(i)
        
        #NSL
        #monotonically increasing stack from left to right
        for i in range(0,n):
            while NSL_stack and nums[NSL_stack[-1]]>nums[i]:
                NSL_stack.pop()
            
            if NSL_stack: NSL[i] = NSL_stack[-1]
            NSL_stack.append(i)
        
        #NSR
        for i in range(n-1,-1,-1):
            while NSR_stack and nums[NSR_stack[-1]]>=nums[i]:
                NSR_stack.pop()
            
            if NSR_stack: NSR[i] = NSR_stack[-1]
            NSR_stack.append(i)
        
        answer = 0
        for i in range(n):
            answer += nums[i] * (NBR[i]-i)*(i-NBL[i])
            answer-= nums[i]*(NSR[i]-i)*(i-NSL[i])
        return answer

        

        