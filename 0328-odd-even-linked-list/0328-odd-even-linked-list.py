# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddNodeHead = ListNode(0,None)
        evenNodeHead = ListNode(0,None)
        oddNodePointer = oddNodeHead
        evenNodePointer = evenNodeHead

        pointer = head
        position=1
        while pointer is not None:
            if position%2==0:
                evenNodePointer.next = pointer
                evenNodePointer = pointer
            else:
                oddNodePointer.next = pointer
                oddNodePointer = pointer
            pointer = pointer.next
            position+=1

        evenNodePointer.next = None
        
        #Link 
        oddNodePointer.next = evenNodeHead.next
        return oddNodeHead.next

