# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy = ListNode(-1,head)
        prev = dummy
        curr = head
        while curr:
            prev_backup = prev
            node_count = curr
            #count number of nodes
            for _ in range(k-1): 
                if node_count.next is None:
                    #this is the last node, return it
                    return dummy.next
                node_count = node_count.next
                
                
                
            for _ in range(k):
                #reverse the first k nodes
                nxt = curr.next
                curr.next = prev

                #move the pointers
                prev = curr
                curr = nxt
            #prev points to last node of this group
            #curr points to new node just right of thsi group
            prev_backup.next.next = curr
            tmp = prev_backup.next
            prev_backup.next = prev
            prev = tmp

        return dummy.next