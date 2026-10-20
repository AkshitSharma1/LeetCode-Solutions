class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        min_flips = float("inf")
        n = len(blocks)
        white_blocks_count = 0 #white blocks in the window
        for r in range(n):
            if blocks[r]=='W': white_blocks_count+=1
            while r-l+1>k:
                if blocks[l]=='W':
                    white_blocks_count-=1
                l+=1
            
            if r-l+1==k:
                min_flips = min(min_flips,white_blocks_count)
        return min_flips


        