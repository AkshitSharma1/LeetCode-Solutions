class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        string = ""
        for word in words:
            string+=word
            if s.startswith(string)==False: return False
            if s==string: return True
        
        return False

        