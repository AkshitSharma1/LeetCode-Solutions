class Solution:
    def maxSumMinProduct(self, nums: list[int]) -> int:
        MOD = 10**9+7
        # our goal is to maximize
        # f(S) = min(S)*(sum(S))
        # Ie S such that f= max over S(min(S)*(sum(S))
        # )

        # Sum(S) will always be positive-> bigger length means more sum
        #NSR,NSL concept to find length of array using this minimum, along with prefix sum for ans
        n = len(nums)

        prefix_sum = [nums[0]]*n
        for i in range(1,n): prefix_sum[i] = prefix_sum[i-1]+nums[i]

        #NSL,NSR
        NSL = [-1]*n
        NSL_stack = []
        NSR = [n]*n
        NSR_stack = []

        #first do NSL-> monotonically increasing stack
        for i in range(n):
            while NSL_stack and nums[NSL_stack[-1]]>=nums[i]:
                NSL_stack.pop()
            
            if NSL_stack: NSL[i] = NSL_stack[-1]
            NSL_stack.append(i)
        #NSR
        for i in range(n-1,-1,-1):
            while NSR_stack and nums[NSR_stack[-1]]>=nums[i]:
                NSR_stack.pop()
            
            if NSR_stack: NSR[i] = NSR_stack[-1]
            NSR_stack.append(i)
        max_min_product = 0
        for i in range(n):
            left_index = NSL[i]
            right_index = NSR[i]
            subarray_length = NSR[i] - NSL[i] -1
            subarray_sum = (prefix_sum[right_index-1])-(0 if left_index==-1 else prefix_sum[left_index])
            max_min_product = max(max_min_product,nums[i]*subarray_sum)
        return max_min_product%MOD


        
