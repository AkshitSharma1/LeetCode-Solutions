# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        queue.append(root)
        answer = []
        while queue:
            lastNodeVal = None
            for _ in range(len(queue)):
                
                currNode = queue.popleft()
                if currNode is None: continue
                lastNodeVal = currNode.val
                queue.append(currNode.left)
                queue.append(currNode.right)
            
            if lastNodeVal is not None: answer.append(lastNodeVal)
        
        return answer


