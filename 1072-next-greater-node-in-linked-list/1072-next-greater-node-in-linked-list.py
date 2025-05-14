# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def reverseLinkList(self,head):
        prev = None
        curr = head
        length = 0
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            length+=1
        return prev, length


    def nextLargerNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """

        newHead,length = self.reverseLinkList(head)
        monotonicStack = []
        pointer = newHead
        NGE = [0]*length
        index = 0
        while pointer is not None:
            
            while len(monotonicStack)!=0 and monotonicStack[-1]<=pointer.val:
                monotonicStack.pop()
            
            if len(monotonicStack)!=0:
                NGE[length-index-1] = monotonicStack[-1]
            monotonicStack.append(pointer.val)
            pointer = pointer.next
            index+=1
        return NGE