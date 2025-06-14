class Solution:
    def numTrees(self, n: int) -> int:
        return int(math.comb(2 * n, n)/(n+1))
        