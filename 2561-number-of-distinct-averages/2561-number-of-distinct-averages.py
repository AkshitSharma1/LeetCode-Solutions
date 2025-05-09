class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        leftPointer = 0
        rightPointer = len(nums)-1
        
        averageSet = set()
        while leftPointer<rightPointer:
            average = (nums[leftPointer]+nums[rightPointer])/2
            averageSet.add(average)
            leftPointer+=1
            rightPointer-=1
        return len(averageSet)
            
            


        