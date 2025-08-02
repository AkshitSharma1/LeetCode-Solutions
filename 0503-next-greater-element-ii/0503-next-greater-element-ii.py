class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        NGR = [-1]*n
        NGRStack = []
        for i in range(n-1,-1,-1):
            while len(NGRStack)>0 and nums[NGRStack[-1]]<=nums[i]:
                NGRStack.pop()
            if len(NGRStack)>0:
                NGR[i] = nums[NGRStack[-1]]
            NGRStack.append(i)
        
        for i in range(n-1,-1,-1):
            while len(NGRStack)>0 and nums[NGRStack[-1]]<=nums[i]:
                NGRStack.pop()
            if len(NGRStack)>0:
                NGR[i] =nums[NGRStack[-1]]
            NGRStack.append(i)
        
        return NGR
        