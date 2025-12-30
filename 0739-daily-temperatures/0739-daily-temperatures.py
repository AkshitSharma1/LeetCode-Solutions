class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ngl = [0]*n
        ngl_stack = []
        for r in range(n-1,-1,-1):
            while ngl_stack and nums[ngl_stack[-1]]<=nums[r]:
                ngl_stack.pop()
            
            if ngl_stack:
                ngl[r] = ngl_stack[-1]-r
            ngl_stack.append(r)
        return ngl