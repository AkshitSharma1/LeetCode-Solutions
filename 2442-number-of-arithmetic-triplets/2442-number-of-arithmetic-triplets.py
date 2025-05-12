import bisect
from typing import List

class Solution:
    def arithmeticTriplets(self, arr: List[int], diff: int) -> int:
        n = len(arr)
        answer = 0
        for start in range(n):
            start_val = arr[start]
            target1 = start_val + diff
            left1 = bisect.bisect_left(arr, target1, lo=start, hi=n)
            right1 = bisect.bisect_right(arr, target1, lo=start, hi=n)
            jth_count = right1 - left1

            target2 = start_val + 2*diff
            left2 = bisect.bisect_left(arr, target2, lo=start, hi=n)
            right2 = bisect.bisect_right(arr, target2, lo=start, hi=n)
            kth_count = right2 - left2

         

            answer += jth_count * kth_count

        return answer
