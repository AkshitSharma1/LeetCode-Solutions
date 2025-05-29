class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        start = 0
        n = len(nums)
        ans = []
        target=0
        while start<n:
            if start>0 and nums[start]==nums[start-1]:
                start+=1
                continue
            
            left = start+1
            right = n-1

            while left<right:
                sumOfValues = nums[left]+nums[right]+nums[start]
                if sumOfValues>target:
                    right-=1
                elif sumOfValues==target:
                    ans.append([nums[start],nums[left],nums[right]])
                    left+=1
                    while left<right and nums[left]==nums[left-1]: left+=1
                else:
                    left+=1
            start+=1
        return ans