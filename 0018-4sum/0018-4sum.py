class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        start = 0
        nums.sort()
        n = len(nums)
        ans = []
        while start<n:
            if start>0 and start<n  and nums[start]==nums[start-1]:
                start+=1
                continue
            

            pointerTwo = start + 1
            while pointerTwo<n:
                if pointerTwo>start+1 and pointerTwo<n and nums[pointerTwo]==nums[pointerTwo-1]:
                    pointerTwo+=1
                    continue
                
                left = pointerTwo+1
                right = n-1
                while left<right:
                    currentSum = nums[start]+nums[pointerTwo]+nums[left]+nums[right]
                    if currentSum>target:
                        right-=1
                    elif currentSum<target:
                        left+=1
                    else:
                        ans.append([nums[start],nums[pointerTwo],nums[left],nums[right]])
                        left+=1
                        right-=1
                        while nums[left]==nums[left-1] and left<right:
                            left+=1
                        while nums[right]==nums[right+1] and left<right:
                            right-=1
                pointerTwo+=1
            start+=1
        return ans

                    

        