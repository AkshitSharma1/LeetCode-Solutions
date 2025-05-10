class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        n = len(nums)
        leftPointer = 0
        rightPointer = n-1
        answer = 0
        while leftPointer<=rightPointer:
            if leftPointer==rightPointer:
                answer+=nums[leftPointer]
            else:
                answer+=(nums[leftPointer]*10**len(str(nums[rightPointer]))+nums[rightPointer])
            rightPointer-=1
            leftPointer+=1
        return answer
        