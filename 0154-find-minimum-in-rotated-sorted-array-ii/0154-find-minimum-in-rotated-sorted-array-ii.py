class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n-1
        while low<high:
            
            #Trim the search space
            while low<n-1 and nums[low]==nums[low+1]: low+=1
            while high>0 and nums[high]==nums[high-1]: high-=1
            
            if low>=high: break


            mid = (low+high)//2

            if nums[mid]<=nums[high]:
                high = mid
            else:
                low = mid+1
            
        return nums[low]