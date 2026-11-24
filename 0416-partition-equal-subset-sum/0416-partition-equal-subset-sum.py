class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        sum_value = sum(nums)
        if sum_value%2!=0: return False
        n = len(nums)

        # f(i,s): if its possible to get the sum s = 0 if we are at the index i
        # we want f(0,sum_value/2) if true or false
        @cache
        def f(i,target):
            if target<0: return False
            if target==0: return True
            if i==n:
                return False

            return f(i+1,target-nums[i]) or f(i+1,target)
        return f(0,sum_value/2)
