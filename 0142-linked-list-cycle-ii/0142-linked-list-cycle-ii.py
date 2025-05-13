# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeSet = set()
        pointer = head
        while pointer is not None:
            if pointer in nodeSet:
                return pointer
            else:
                nodeSet.add(pointer)
            pointer = pointer.next
        
        return None
        