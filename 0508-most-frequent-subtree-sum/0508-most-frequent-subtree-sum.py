# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode | None) -> list[int]:
        sum_freq = defaultdict(int) #frequency of sum , we want sum corresponding to max freq

        def subtreeSum(node):
            nonlocal sum_freq
            if node is None: return 0
            subtree_sum = node.val + subtreeSum(node.left) + subtreeSum(node.right)
            sum_freq[subtree_sum]+=1
            return subtree_sum
        
        subtreeSum(root)
        max_freq = max(sum_freq.values())
        answer = []
        for subtree_sum,freq in sum_freq.items():
            if freq==max_freq:
                answer.append(subtree_sum)
        return answer

        