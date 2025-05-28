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
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next
            if fastPointer==slowPointer: return True
        return False
        