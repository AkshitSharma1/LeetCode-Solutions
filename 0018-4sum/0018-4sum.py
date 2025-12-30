class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        current_sum = 0
        p,q,l,r = 0,0,0,0
        answer = []
        nums.sort()
        n = len(nums)
        for p in range(n):
            if p>0 and nums[p]==nums[p-1]: continue
            for q in range(p+1,n):
                if q>p+1 and nums[q]==nums[q-1]: continue
                l = q+1
                r = n-1
                while l<r:
                    current_sum = nums[p]+nums[q]+nums[l]+nums[r]
                    if current_sum>target:
                        r-=1
                    elif current_sum<target:
                        l+=1
                    else:
                        answer.append([nums[p],nums[q],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l>q+1 and l<n and nums[l]==nums[l-1]: 
                            l+=1
                        while r<n-1 and r>=0 and nums[r]==nums[r+1]:
                            r-=1
        return answer
                    