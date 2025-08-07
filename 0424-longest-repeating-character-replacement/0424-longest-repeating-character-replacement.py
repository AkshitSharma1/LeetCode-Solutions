class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        frequencyMap = defaultdict(int)
        l = 0
        n = len(s)
        maxFrequencyChar = 0
        for r,char in enumerate(s):
            frequencyMap[char]+=1
            maxFrequencyChar = max(maxFrequencyChar,frequencyMap[char])
            while r-l+1-maxFrequencyChar>k:
                frequencyMap[s[l]]-=1
                l+=1
            
            maxLength = max(maxLength,r-l+1)
        return maxLength