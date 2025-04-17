# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # dummy node before the result
        # this is an empty node as we always update the next pointer of curr (starting at res) to add new nodes
        curr = dummy # pointer to the current node in the result
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            s = v1 + v2 + carry
            carry = s // 10
            val = s % 10
            # we want to link new node to curr.next and move curr forward
            curr.next = ListNode(val) # create a new node
            curr = curr.next # move the pointer to the next node
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next # dummy.next points to the first valid node of the result while dummy is just a dummy node
