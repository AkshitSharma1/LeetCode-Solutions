# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode | None) -> bool:
        def bfs(node):
            queue = deque([(node,0)])
            none_seen = False #if null node seen before or not
            while queue:
                curr_level = queue[0][1]
                for _ in range(len(queue)):
                    curr_node,curr_level = queue.popleft()
                    
                    #handle the case when curr_node is none
                    # this must occur at the last level only and must be continuous once occured
                    if curr_node is None:
                        none_seen = True
                        continue
                    #we see a node after seeing a none-> not complete tree
                    if node is not None and none_seen==True:
                        return False
                    


                    #first lets write code to append child
                    queue.append((curr_node.left,curr_level+1))
                    queue.append((curr_node.right,curr_level+1))
            return True
        return bfs(root)