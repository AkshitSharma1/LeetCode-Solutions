from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        left=0
        ans = []
        for right in range(len(nums)):
            while len(queue)>0 and nums[queue[-1]]<nums[right]:
                queue.pop()
            queue.append(right)
            
            if right-left+1>=k:
                ans.append(nums[queue[0]])
                if queue[0]<=left:
                    queue.popleft()
                left+=1
        return ans


        