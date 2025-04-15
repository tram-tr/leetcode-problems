# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return

        # left -> k
        # right -> (n - k + 1)
        # using two pointers (fast and slow)
        fast = slow = head

        # use fast pointer to find the k-th node from the beginning
        # move fast pointer ahead k-1 times
        for _ in range(k - 1): # the list is 1-indexed
            fast = fast.next

        # once we have the fast pointer on th k-th node from the start
        # there are n-k nodes from the there to the end
        # therefore by the time fast goes to those remaining n-k to the ends
        # slow will have gone n-k steps forward from the head, placing it at 
        # n-k+1 position which is the k-th node from the end

        # use slow pointer to find the k-th node from the end
        # use a slow pointer to start from the head node of the linked list
        # and move both pointers at the same time
        # when the fast pointers reaches the last node of the linked list, 
        # the slow pointer slow points to the k-th node from the end of the linked list


        left = fast
        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        right = slow

        left.val, right.val = right.val, left.val

        return head
        
        

        
        
