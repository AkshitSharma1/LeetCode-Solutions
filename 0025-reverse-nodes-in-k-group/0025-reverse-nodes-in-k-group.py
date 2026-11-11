# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        #we first ensure more than k nodes are there
        #if yes, then we reverse first group
        # we connect node prior to the group start with the last node of group
        # we connect first node of group to the first node after the group ends
        dummy = ListNode(-1,head)
        prev = dummy
        curr = head

        #first ensure k nodes
        node_count = prev
        for _ in range(k):
            node_count = node_count.next
            if node_count is None:
                #nothing to reverse
                return dummy.next
        
        #now actually reverse the k nodes
        prev_backup = prev #node just before the group
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        #now connect the messed up pointers
        tmp = prev_backup.next
        prev_backup.next.next = self.reverseKGroup(curr,k)
        prev_backup.next = prev

        #now setup prev and curr correctly
        prev = tmp
        return dummy.next