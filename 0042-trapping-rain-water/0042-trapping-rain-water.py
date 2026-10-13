class Solution:
    def trap(self, height: list[int]) -> int:
        pi_height = height[0]
        n = len(height)
        pj_height = height[n-1]
        pi = 0
        pj = n-1
        ans = 0
        while pi<pj:
            pi_height = max(height[pi],pi_height)
            pj_height = max(height[pj],pj_height)
            if pi_height<=pj_height:
                ans += pi_height-height[pi]
                pi+=1
            else:
                ans+=pj_height-height[pj]
                pj-=1
        return ans
            

        