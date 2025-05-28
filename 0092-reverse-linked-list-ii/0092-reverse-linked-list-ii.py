# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        position=1
        curr = dummy.next
        prev = dummy
        while position<left:
            nxtBackup = curr.next
            prev = curr
            curr = nxtBackup
            position+=1


        #prev = node just before left node
        nodeJustBeforeLeft = prev
        #Reverse the next right-left+1 nodes
        
        for _ in range(right-left+1):
            nextNodeBackup = curr.next
            curr.next = prev
            prev = curr
            curr = nextNodeBackup
            
        nodeJustBeforeLeft.next.next = curr
        nodeJustBeforeLeft.next = prev

        return dummy.next

        