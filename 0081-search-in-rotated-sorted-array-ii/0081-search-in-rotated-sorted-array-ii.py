class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        l = 0
        n = len(nums)
        r = n-1
        while l<=r:
            mid = (l+r)//2
           
            
            if nums[mid]==target: return True

            if nums[mid]==nums[r]:
                r-=1
                continue
            if nums[mid]==nums[l]:
                l+=1
                continue


            if nums[mid]<nums[r]:
                if nums[mid]<=target<=nums[r]:
                    l = mid+1
                else:
                    r = mid-1
            else:
                #left portion is sorted 
                if nums[l]<=target<=nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
        return False
