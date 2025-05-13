from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        monotonicQueue = deque()
        i=0
        answer=[]
        for j in range(len(nums)):
            while len(monotonicQueue)!=0 and nums[monotonicQueue[-1]]<=nums[j]:
                monotonicQueue.pop()
            monotonicQueue.append(j)

            if j-i+1==k:
                #Process the window
                answer.append(nums[monotonicQueue[0]])
                #Move the window
                while len(monotonicQueue)!=0 and monotonicQueue[0]<=i:
                    monotonicQueue.popleft()
                i+=1
        return answer
            

        