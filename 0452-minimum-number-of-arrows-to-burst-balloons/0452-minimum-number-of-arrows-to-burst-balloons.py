class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x:x[0])
        prev_start = prev_end = float("-inf")
        arrows_required = 0
        for curr_start,curr_end in points:
            if curr_start>prev_end:
                prev_start = curr_start
                prev_end = curr_end
                arrows_required +=1
            else:
                prev_start = max(prev_start,curr_start)
                prev_end = min(prev_end,curr_end)

        return arrows_required