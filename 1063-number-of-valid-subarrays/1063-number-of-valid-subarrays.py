class Solution:
    def validSubarrays(self, nums: list[int]) -> int:
        #leftmost element must be smaller than the elements in the array
        #find next smaller element index to the right-> all numbers before this form a sub array
        NSR_stack = []
        n = len(nums)
        NSR = [n]*n
        #monotonically incresing stack 
        for i in range(n-1,-1,-1):
            while NSR_stack and nums[NSR_stack[-1]]>= nums[i]:
                NSR_stack.pop()
            
            if NSR_stack: NSR[i] = NSR_stack[-1]
            NSR_stack.append(i)
        
        answer = 0 #count 
        for i in range(n):
            answer += NSR[i]-i
        return answer
        