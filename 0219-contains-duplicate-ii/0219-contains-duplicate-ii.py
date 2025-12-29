class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen_index = defaultdict(lambda:-1)
        for i,num in enumerate(nums):
            if last_seen_index[num]==-1:
                last_seen_index[num]=i
            else:
                difference = i - last_seen_index[num]
                if abs(difference)<=k: return True
                last_seen_index[num] = i
        return False

        
