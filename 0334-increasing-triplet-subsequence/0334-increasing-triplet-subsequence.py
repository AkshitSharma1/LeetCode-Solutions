class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        # assign nums[i] = 1 , nums[j] = 2, nums[k] = 3
        #then i<j<k becomes 1 2 3 pattern
        n = len(nums)
        NSL = [-1]*n
        nsl_stack = []
        nbr_stack = []
        NBR = [n]*n
        #first populate NSL-> let to right, monotonically increasing stack
        #for NBR-> right to left, monotonically decreasing stack
        #NSL
        for i in range(n):
            while nsl_stack and nums[nsl_stack[-1]]>=nums[i]:
                nsl_stack.pop()
            if nsl_stack: NSL[i] = nsl_stack[-1]
            nsl_stack.append(i)

        #NBR
        for i in range(n-1,-1,-1):
            while nbr_stack and nums[nbr_stack[-1]]<=nums[i]:
                nbr_stack.pop()
            if nbr_stack: NBR[i] = nbr_stack[-1]
            nbr_stack.append(i)


        for j in range(len(nums)):
            if NSL[j]!=-1 and NBR[j]!=n: return True
        
        return False


