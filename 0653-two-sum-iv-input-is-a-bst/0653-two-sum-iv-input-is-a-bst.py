# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self,nodeValues,currentNode):
        if currentNode is None: return
        self.inorderTraversal(nodeValues,currentNode.left)
        nodeValues.append(currentNode.val)
        self.inorderTraversal(nodeValues,currentNode.right)
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nodeValues = []
        self.inorderTraversal(nodeValues,root)
        i=0
        j = len(nodeValues)-1
        while i<j:
            leftNode = nodeValues[i]
            rightNode = nodeValues[j]
            if leftNode+rightNode>k:
                j-=1
            elif leftNode+rightNode<k:
                i+=1
            else: return True
        return False


        
        