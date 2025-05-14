# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None: return None
        length = 0
        pointer = head
        rotate = k
        while pointer is not None:
            pointer = pointer.next
            length+=1

        
        rotate%=length

        dummyHead = ListNode(0,head)
        for rotation in range(rotate):
            pointer = dummyHead.next
            prev = dummyHead
            while pointer.next is not None:
                prev = pointer
                pointer = pointer.next
            
            prev.next = None
            pointer.next = dummyHead.next
            dummyHead.next = pointer
        
        return dummyHead.next



        