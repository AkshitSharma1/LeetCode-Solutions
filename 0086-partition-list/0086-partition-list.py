# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smallerElementQueue = deque()
        largerElementQueue = deque()
        
        pointer = head
        while pointer is not None:
            if pointer.val<x: 
                smallerElementQueue.append(pointer.val)
            else:
                largerElementQueue.append(pointer.val)
            pointer = pointer.next

        dummyHead = ListNode(0,None)
        pointer = dummyHead
        while len(smallerElementQueue)>0:
            pointer.next = ListNode(val=smallerElementQueue.popleft(),next=None)
            pointer = pointer.next

        while len(largerElementQueue)>0:
            pointer.next = ListNode(val=largerElementQueue.popleft(),next=None)
            pointer = pointer.next
        
        return dummyHead.next
        
        


            