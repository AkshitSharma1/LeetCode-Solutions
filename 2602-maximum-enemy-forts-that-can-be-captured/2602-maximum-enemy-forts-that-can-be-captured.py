class Solution:
    def captureForts(self, forts: List[int]) -> int:
        count = 0
        left = 0
        for right in range(1,len(forts)):
            if forts[right] != 0:
                if (forts[left] == 1 and forts[right] == -1) or (forts[left] == -1 and forts[right] ==1):
                    count = max(count, right - left - 1)
                left = right
        return count