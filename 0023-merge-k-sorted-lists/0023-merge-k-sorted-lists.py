# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        for index,linkedList in enumerate(lists):
            if linkedList is None: continue
            heapq.heappush(heap,(linkedList.val,index,linkedList))
        dummy = ListNode(0,None)
        pointer = dummy
        while len(heap)!=0:
            topList = heapq.heappop(heap)
            pointer.next = ListNode(topList[0],None)
            pointer = pointer.next
            if topList[2].next is not None:
                heapq.heappush(heap,(topList[2].next.val,topList[1],topList[2].next))
        
        return dummy.next
                

            

        