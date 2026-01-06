class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        @lru_cache(maxsize=512)
        def can_segment(index):
            nonlocal s
            n = len(s)
            if index>=n: return True
            current_s =""
            for i in range(index,n,1):
                current_s+=s[i]
                if current_s in wordSet and can_segment(i+1): return True
            return False

        return can_segment(0)
                
        