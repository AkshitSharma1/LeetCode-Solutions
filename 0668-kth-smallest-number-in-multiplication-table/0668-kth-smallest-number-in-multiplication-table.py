class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        l = 0
        r = m * n

        def countProductsLessEqual(x):
            count = 0

            for i in range(1, m + 1):
                count += min(n, x // i)

            return count

        ans = float("inf")

        while l <= r:
            mid = (l + r) // 2

            products_lessequal_m_count = countProductsLessEqual(mid)

            if products_lessequal_m_count >= k:
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1

        return ans