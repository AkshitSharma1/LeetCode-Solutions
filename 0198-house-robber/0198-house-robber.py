class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def f(i):
            if i>=n: return 0
            ans = max(nums[i] + f(i+2),
            f(i+1))
            return ans
        return f(0)

