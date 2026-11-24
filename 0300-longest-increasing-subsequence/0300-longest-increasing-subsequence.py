class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # [10,7,11,15]
        # for any number i in nums:
        #     you loop back, check which numbers are less than i
        #     1 + max(length of subsequence that ends at j, where j < i )
        #     f(i) = length of longest subsequence that ends at i
        #     f(i) = 1 + max (f(j)) for all j<i

        @cache
        def f(i):
            #length of lis which ends at num[i]
            if i==0: return 1
            ans = 1
            for j in range(i-1,-1,-1):
                if nums[j]>=nums[i]: continue
                ans = max(ans,1+f(j))
            return ans

        return max([f(i) for i in range(0,len(nums))])