# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = ListNode(0,head)
        start = prevNode
        currNode = head
        nextNode = head.next if head is not None else None
        while nextNode is not None:
          

            #move all front by one
            currNodeBackup = currNode.next.next if currNode is not None and currNode.next is not None and currNode.next.next is not None else None
            nextNodeBackup = nextNode.next.next if nextNode is not None and nextNode.next is not None and nextNode.next.next is not None else None
            prevNodeBackup = prevNode.next if prevNode is not None and prevNode.next is not None else None
            
            # handle middle node case
            currNode.next = nextNode.next
            nextNode.next = currNode
            prevNode.next = nextNode

            currNode = currNodeBackup
            nextNode = nextNodeBackup
            prevNode = prevNodeBackup
        return start.next
        