class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = 0
        n = len(nums)
        r = n -1
        ans = float("inf")
        while l<=r:
            mid = (l+r)//2
            if nums[mid]<=nums[r]:
                ans = min(ans,nums[mid])
                r = mid-1
            else:
                l = mid+1
        return ans


