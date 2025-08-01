class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        for start in range(len(nums)):
            if start>0 and nums[start]==nums[start-1]: continue
            l,r = start+1,len(nums)-1
            while l<r:
                currentSum = nums[start]+nums[l]+nums[r]
                if currentSum==0:
                    answer.append([nums[start],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]: l+=1
                    while l<r and nums[r]==nums[r+1]: r-=1
                elif currentSum>0:
                    r-=1
                else:
                    l+=1
        return answer