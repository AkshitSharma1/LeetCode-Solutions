# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        last_node = head
        if head is None: return None
        while last_node and last_node.next: last_node = last_node.next
        last_node_pointer = last_node #points to the same last node
        #points to last node
        i = 1
        prev = None
        curr = head
        #
        while curr is not last_node.next:
            if i%2==0:
                #we will be removing this curr node, inserting it to the last node
                last_node_pointer.next = ListNode(curr.val,None)
                last_node_pointer = last_node_pointer.next

                #now remove current node
                prev.next = curr.next
                curr = curr.next
            else:
                #just move
                prev = curr
                curr = curr.next

            i+=1
        return head


        