class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        n = len(nums)
        if n==1: return 0
        while low<=high:
            mid = (low+high)//2
            if mid>0 and mid<n-1:
                if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]: 
                    return mid
                elif nums[mid]>nums[mid-1] and nums[mid]<nums[mid+1]:
                    low = mid+1
                
                else:
                    high = mid-1
            else:
                if mid==0:
                    if nums[mid]<nums[mid+1]:
                        low = mid+1
                    else: return mid
                
                elif mid==n-1:
                    if nums[mid]<nums[mid-1]:
                        high = mid-1
                    else:
                        return mid
        
        return -1