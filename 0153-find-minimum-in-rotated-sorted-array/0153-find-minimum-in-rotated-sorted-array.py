class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n-1
        ans = float("inf")

        while l<=r:
            mid = (l+r)//2
            ans = min(ans,nums[mid])
            if nums[mid]<=nums[r]:
                r = mid-1
            else:
                l = mid+1
        return ans
        