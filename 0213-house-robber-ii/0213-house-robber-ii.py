class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if len(nums)==1: return nums[0]
        @cache
        def f(i,n):
            #basecases
            if i>n: return 0
            answer = max(nums[i] + f(i+2,n), f(i+1,n))
            return answer
        return max(f(0,length-2),f(1,length-1))
        

