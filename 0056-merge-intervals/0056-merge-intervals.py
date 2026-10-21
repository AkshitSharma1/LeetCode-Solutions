class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        ans = []
        intervals.sort(key=lambda x:(x[0],x[1]))
        for curr_start,curr_end in intervals:
            if not ans or curr_start>ans[-1][1]:
                ans.append([curr_start,curr_end])
            else:
                ans[-1][1] = max(ans[-1][1],curr_end)
        return ans