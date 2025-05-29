class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        ans = 0
        while low<high:
            mid = (low+high)//2
            
            #C1
            if  nums[high]<=nums[mid]:
                low = mid+1
            elif nums[mid]<=nums[high]:
                high = mid
                ans = nums[mid]
                #Possible answer
            
        return nums[low]