from collections import deque
from typing import List

class Solution:
    def findIndices(self,
                    nums: List[int],
                    indexDifference: int,
                    valueDifference: int
                   ) -> List[int]:
        n = len(nums)

        max_deque = deque()
        min_deque = deque()

 
        for i in range(n):
            # 1) Add the new index j = i - indexDifference into both deques
            j = i - indexDifference
            if j >= 0:
                v = nums[j]
                while max_deque and max_deque[-1][0] < v:
                    max_deque.pop()
                max_deque.append((v, j))

                while min_deque and min_deque[-1][0] > v:
                    min_deque.pop()
                min_deque.append((v, j))

            if max_deque:
                max_v, max_j = max_deque[0]
                if max_v >= nums[i] + valueDifference:
                    return [max_j, i]

            if min_deque:
                min_v, min_j = min_deque[0]
                if min_v <= nums[i] - valueDifference:
                    return [min_j, i]

        return [-1, -1]
