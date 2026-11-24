class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # f(i) = whether the portion [0:i] of string s is present in dictionry either as a whole or in parts
        wordDict = set(wordDict)
        @cache
        def f(i):
            if i==0:
                return True
            for j in range(i-1,-1,-1):
                if f(j) and s[j:i] in wordDict:
                    return True
            
            return False
        
        return f(len(s))

