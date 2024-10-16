class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        finalAns = []
        def solve(index,temp):
            if index==len(nums): 
                finalAns.append(list(temp))
                return
            for i in range(len(nums)):
                if nums[i]!=11:
                    tempVar = nums[i]
                    temp.append(nums[i])
                    nums[i]=11
                    solve(index+1,temp)
                    temp.pop()
                    nums[i] = tempVar
        solve(0,[])
        return finalAns
        