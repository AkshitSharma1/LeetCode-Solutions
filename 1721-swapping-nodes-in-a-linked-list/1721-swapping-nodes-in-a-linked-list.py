# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #for kth node from end-> use fast and slow pointer
        dummy = ListNode(-1,head)
        slow = fast = dummy
        for _ in range(k): fast = fast.next if fast.next is not None else None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        kthNodeFromEnd = slow.next
        #kth node from start-

        slow = head
        for _ in range(k-1): 
            slow = slow.next
        kthNodeFromStart = slow
        kthNodeFromStart.val, kthNodeFromEnd.val = kthNodeFromEnd.val, kthNodeFromStart.val
        return dummy.next
