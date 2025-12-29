class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = defaultdict(int)
        max_char_count = 0
        max_char = ''
        l = 0
        answer = 0
        for r,char in enumerate(s):
            char_count[char]+=1
            max_char_count = max(char_count[char],max_char_count)
            
            number_of_chars_to_replace = r-l+1-max_char_count
            while r-l+1-max_char_count>k:
                char_count[s[l]]-=1
                l+=1
            
            answer = max(answer,r-l+1)
        return answer