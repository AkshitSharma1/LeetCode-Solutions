class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        ans = -1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid

            if nums[mid]<=nums[r]:
                if nums[mid]<=target and target<=nums[r]:
                    l = mid+1
                else:
                    r = mid-1
            else:
                if nums[l]<=target and nums[mid]>=target:
                    r = mid-1
                else:
                    l= mid+1
        return -1 
        