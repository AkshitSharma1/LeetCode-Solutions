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

        while pointer is not None:
            length+=1
            pointer = pointer.next
        dummyHead = ListNode(0,head)
        for _ in range(k%length):
            #Bring the last node to the front 
            lastNodePointer = dummyHead.next
            secondLastNodePointer = dummyHead
            while lastNodePointer.next is not None:
                secondLastNodePointer = lastNodePointer
                lastNodePointer = lastNodePointer.next
            
            #Now bring the last node to front
            secondLastNodePointer.next = None
            lastNodePointer.next = dummyHead.next
            dummyHead.next = lastNodePointer
        
        return dummyHead.next

        




        