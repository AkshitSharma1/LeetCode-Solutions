class Solution:
    def mostCompetitive(self, nums: list[int], k: int) -> list[int]:
        deletions_allowed = len(nums)-k

        stack = []
        for num in nums:
            while stack and stack[-1]>num and deletions_allowed>0:
                stack.pop()
                deletions_allowed -= 1
            stack.append(num)
        while deletions_allowed>0:
            stack.pop()
            deletions_allowed-=1
        return stack
        