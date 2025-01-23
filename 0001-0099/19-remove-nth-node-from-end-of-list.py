# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(None, head)

        for _ in range(n):
            head = head.next

        curr = res
        while head:
            head = head.next
            curr = curr.next

        curr.next = curr.next.next
        new_head = res.next

        return new_head
