class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
     
        slow = fast = nums[0]
        hasMetBefore = False
        while fast:
            slow = nums[slow]
            fast = nums[nums[fast]] if hasMetBefore==False else nums[fast]
            if slow==fast:
                #if have met before
                if hasMetBefore:
                    return slow
                else:
                    hasMetBefore = True
                    fast = nums[0]
                    if slow==fast: return slow
        return -1