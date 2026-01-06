class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        n = len(s)
        answer = []
        @lru_cache(None)
        def dp(index):
            nonlocal s,n
            if index>=n: return [""]
            temp_ans = []
            for i in range(index,n,1):
                word = s[index:i+1]
                tails = dp(i+1)

                if word in word_set and tails:
                    temp_ans.extend(word + ("" if tail == "" else " " + tail) for tail in tails)

            return temp_ans
        return dp(0)


            
