# https://leetcode.com/problems/merge-k-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        min_heap = []
        heapify(min_heap)
        
        # push all smallest to the heap
        for head in lists:
            if head is not None:
                heappush(min_heap, (head.val, head))
        
        merged_head = None
        merged_tail = None

        while len(min_heap) > 0:
            _, node = heappop(min_heap)
            if merged_head is None: # start of the merged linked list
                merged_tail = node 
                merged_head = merged_tail
            else:
                merged_tail.next = node
                merged_tail = merged_tail.next
            
            if node.next is not None:
                heappush(min_heap, (node.next.val, node.next))

        return merged_head
    