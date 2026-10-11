from collections import defaultdict

class Solution:
    def maxEqualFreq(self, nums: list[int]) -> int:
        group_by_freq = dict()
        num_count = defaultdict(int)
        ans = 0

        for r, num in enumerate(nums):
            num_count[num] += 1
            freq = num_count[num]

            if freq not in group_by_freq:
                group_by_freq[freq] = set()

            if freq > 1:
                group_by_freq[freq - 1].remove(num)
                if len(group_by_freq[freq - 1]) == 0:
                    del group_by_freq[freq - 1]

            group_by_freq[freq].add(num)

            if len(group_by_freq) == 1:
                if 1 in group_by_freq or len(next(iter(group_by_freq.values()))) == 1:
                    ans = r + 1

            if len(group_by_freq) == 2:
                min_freq = min(group_by_freq)
                max_freq = max(group_by_freq)

                if max_freq == min_freq + 1:
                    if len(group_by_freq[max_freq]) == 1:
                        ans = r + 1

                if min_freq == 1:
                    if len(group_by_freq[min_freq]) == 1:
                        ans = r + 1

        return ans