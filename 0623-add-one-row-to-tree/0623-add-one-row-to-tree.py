# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, target_depth: int) -> Optional[TreeNode]:
        #bfs
        if root is None: return None
        if target_depth==1:
            new_root = TreeNode(val=val,left=root)
            return new_root

        queue = deque([(root,1)]) #node, depth
        while queue:
            #process all nodes at same depth
            for _ in range(len(queue)):
                node,depth = queue.popleft()
                
                if depth==target_depth-1:
                    #take a backup
                    backup = node.left
                    node.left = TreeNode(val=val,left=backup)
                    backup = node.right
                    node.right = TreeNode(val=val,right=backup)
                    continue

        

                if node.left:
                    queue.append((node.left,depth+1))
                
                if node.right:
                    queue.append((node.right,depth+1))
        return root
                

