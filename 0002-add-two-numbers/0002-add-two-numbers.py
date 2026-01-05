# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        p1 = l1
        p2 = l2
        dummy = ListNode(-1)
        curr = dummy
        while p1 or p2 or carry:
            s = (p1.val if p1 else 0) + (p2.val if p2 else 0) + carry
            carry = s//10
            s%=10
            curr.next = ListNode(val=s)
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
            curr = curr.next
        return dummy.next
            
