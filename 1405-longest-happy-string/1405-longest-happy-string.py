class Solution:
    def _get_max_freq_char(self,freq_count,avoid_char='X'):
        for char,freq in freq_count.most_common():
            if char==avoid_char:
                continue
            else:
                if freq!=0:
                    freq_count[char]-=1
                    return char
        return '-1'

    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        # (frequency_count, char) of size 3
        frequency_count = Counter({"a":a,"b":b,"c":c})
        s = ""
        while True:
            avoid_char = None
            if s and len(s)>=2 and s[-2]==s[-1]:
                avoid_char = s[-1]
            get_next_char = self._get_max_freq_char(frequency_count,avoid_char)
            if get_next_char=='-1':
                return s
            else:
                s+= get_next_char
        return -1
    
             
