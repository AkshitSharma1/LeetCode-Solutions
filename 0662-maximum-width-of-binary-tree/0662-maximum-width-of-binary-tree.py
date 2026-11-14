# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        ans = -1
        def levelOrderTraversal(node):
            nonlocal ans
            queue = deque([(node,1)]) #(node,index position)
            level = []


            while queue:
                #indexes for the current level
                first_node_index = -1
                last_node_index = -1
                for _ in range(len(queue)):
                    curr,index = queue.popleft()
                    if first_node_index==-1: first_node_index = index
                    last_node_index = index
                    ans = max(ans,last_node_index-first_node_index+1)
                    if curr.left:
                        queue.append((curr.left,2*index))
                    if curr.right:
                        queue.append((curr.right,2*index+1))
        levelOrderTraversal(root)
        return ans
            

        