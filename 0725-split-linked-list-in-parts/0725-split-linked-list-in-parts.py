# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        pointer = head
        length = 0
        array = []
        while pointer is not None:
            length+=1
            pointer = pointer.next

        dummyHead = ListNode(0,head)
        prev, curr = dummyHead,head
        for partIndex in range(k):
            remainingParts = k-partIndex
            currentPartLength = math.ceil(length/remainingParts)
            length -= currentPartLength
            currBackup = curr
            
            for _ in range(currentPartLength):
                if curr is None: break

                prev = curr
                curr = curr.next
            
            prev.next = None
            
            array.append(currBackup)
        
        return array

                
                

        