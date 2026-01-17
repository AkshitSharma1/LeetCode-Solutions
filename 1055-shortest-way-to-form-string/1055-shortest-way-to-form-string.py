class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        char_pos = defaultdict(list)
        for i,ch in enumerate(source): char_pos[ch].append(i)
        target_index = 0
        src_index = -1
        curr_substr_length = 0
        answer = 0
        while target_index<len(target):
            target_ch = target[target_index]
            if target_ch not in char_pos: return -1
            src_pos = char_pos[target_ch]
            index = bisect_right(src_pos,src_index)
            if index==len(src_pos):
                #we cant make use of source further to make substring
                src_index = -1
                answer+=1
                curr_substr_length = 0
            else:
                src_index = src_pos[index]
                curr_substr_length +=1
                target_index+=1
        
        if curr_substr_length>0: answer+=1
        return answer


            
        