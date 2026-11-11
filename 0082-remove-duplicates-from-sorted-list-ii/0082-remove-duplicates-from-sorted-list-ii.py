# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:

        dummy = ListNode(-1,head)
        curr = dummy
        while curr and curr.next:
            next_node = curr.next
            duplicate_value_count = 0
            while next_node and next_node.next and next_node.next.val==next_node.val:
                #find the finishing node of the duplicates (ie last node)
                next_node = next_node.next
                duplicate_value_count+=1
            
            #next_node now points to the last node of duplicates (if its there)
            if duplicate_value_count==0:
                #no duplicates for next value
                #-> safely increment the curr
                curr = next_node
            else:
                curr.next = next_node.next

        return dummy.next

        