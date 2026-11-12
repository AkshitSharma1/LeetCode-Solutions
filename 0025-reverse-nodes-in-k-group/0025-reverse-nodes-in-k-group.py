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

        #we perform reversal
        while curr:
            #see if we have k nodes or not in front of us
            node_counter = prev
            for _ in range(k):
                node_counter = node_counter.next
                if node_counter is None:
                    #no need to reverse, just return the answer
                    return dummy.next

            #reverse the k nodes
            prev_backup = prev
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            #now previous points to last node of this group (which logically will be first node of reversed group)
            #curr points to node just after it (prev_backup.next gives us last node of reversed group)
            last_new_group_node = prev_backup.next
            prev_backup.next.next = curr
            prev_backup.next = prev

            #move the pointers ahead
            prev = last_new_group_node
        return dummy.next

        