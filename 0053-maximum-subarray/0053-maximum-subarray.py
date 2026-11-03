class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        k1 = float("-inf")
        ans = float("-inf")
        k2 = float("-inf")
        for r,num in enumerate(nums):
            k1 = max(num,k1+num)
            ans = max(k1,ans)
        return ans