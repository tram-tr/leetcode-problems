# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res = 0
        # iterating through the linked list
        # shifting the current res to the left by one bit and adding the current node's value
        # this is equivalent to multiplying the current res by 2 and adding the current node's value
        # res = 0
        # head->[1]->[0]->[1]->None
        # res = 0 << 1 | 1 = 0 | 1 = 1
        # res = 1 << 1 | 0 = 2(10) | 0 = 2(10)
        # res = 2(10) << 1 | 1 = 4(100) | 1 = 5(101)
        while head is not None:
            res = res << 1 | head.val
            head = head.next

        return res
