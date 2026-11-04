class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        n = len(nums)
        NSL = [-1]*n
        NSR = [n]*n
        NSL_stack = []
        NSR_stack = []
        #NSL-> monotonic increasing stack
        for i in range(n):
            while NSL_stack and nums[NSL_stack[-1]]>=nums[i]: NSL_stack.pop()
            if NSL_stack: NSL[i] = NSL_stack[-1]
            NSL_stack.append(i)
        
        #NSR
        for i in range(n-1,-1,-1):
            while NSR_stack and nums[NSR_stack[-1]]>=nums[i]: NSR_stack.pop()
            if NSR_stack: NSR[i] = NSR_stack[-1]
            NSR_stack.append(i)
        
        ans = 0
        for i in range(n):
            ans = max(ans,nums[i]*(NSR[i]-1-(NSL[i]+1)+1) if (NSL[i]+1)<=k and k<=(NSR[i]-1)
            else 0
            )
        return ans
