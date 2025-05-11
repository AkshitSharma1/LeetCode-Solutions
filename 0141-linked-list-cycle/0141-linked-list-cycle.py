# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowPointer = head
        fastPointer = head
        while fastPointer is not None and fastPointer.next is not None:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
            if slowPointer==fastPointer: return True
        return False
        