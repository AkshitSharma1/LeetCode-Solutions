# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], N: int) -> Optional[ListNode]:
        #First find length of linkedList
        dummy = ListNode(0,head)
        pointer = dummy
        fastPointer = head

        

        for i in range(N): 
            fastPointer = fastPointer.next
        
        while fastPointer is not None:
            fastPointer = fastPointer.next
            pointer = pointer.next
        
        pointer.next = pointer.next.next

        return dummy.next




        