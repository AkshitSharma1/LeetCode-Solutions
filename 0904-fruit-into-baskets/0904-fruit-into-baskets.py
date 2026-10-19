class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        picked_fruit_type_freq = defaultdict(int)
        max_pick = 0
        current_pick = 0
        l = 0
        for r,fruit_type in enumerate(fruits):
            picked_fruit_type_freq[fruit_type]+=1
            current_pick +=1
            while len(picked_fruit_type_freq)>2:
                picked_fruit_type_freq[fruits[l]]-=1
                if picked_fruit_type_freq[fruits[l]]==0:
                    del picked_fruit_type_freq[fruits[l]]
                current_pick -=1
                
                l+=1
            max_pick = max(max_pick,current_pick)
        return max_pick

        