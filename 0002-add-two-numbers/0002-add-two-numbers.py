# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1Pointer = l1
        l2Pointer = l2
        dummy = ListNode(0,None)
        head = dummy
        carry=0
        while l1Pointer is not None or l2Pointer is not None:

            sumOfValues = (l1Pointer.val if l1Pointer is not None else 0)+(l2Pointer.val if l2Pointer is not None else 0)
            remainder = sumOfValues
            dummy.next = ListNode((remainder+carry)%10,None)
            dummy = dummy.next
            carry = (remainder+carry)//10


            l1Pointer = l1Pointer.next if l1Pointer is not None else None
            l2Pointer = l2Pointer.next if l2Pointer is not None else None

        if carry!=0:
            dummy.next = ListNode(1,None)
        
        return head.next

        