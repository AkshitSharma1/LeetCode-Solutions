class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        left,right=1,1
        while right<len(nums):
            while right<len(nums) and nums[right]==nums[right-1]:
                right+=1
            if right==len(nums): break
            nums[left] = nums[right]
            left+=1
            right+=1
        
        low = 0
        high = left-1
        while low<=high:
            mid = (low+high)//2

            if nums[mid]==target: return True
            elif nums[low]<=nums[mid]:
                #This portion is sorted
                if nums[low]<=target and nums[mid]>=target:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if nums[mid]<=target and target<=nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return False
        
        