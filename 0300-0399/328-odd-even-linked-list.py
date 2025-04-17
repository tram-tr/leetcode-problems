# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        if not head or not head.next or not head.next.next:
            return head

        '''
        1 -> 2 -> 3 -> 4 -> 5

        1(odd) -> 2(even) -> 3 -> 4 -> 5 -> None
        odd chain: 1 -> 3 (odd)
        even chain: 2 -> 4 (even)

        odd chain: 1 -> 3 -> 5(odd)
        even chain: 2(temp) -> 4 -> None (even)

        link odd-even chain: odd.next = temp
        1 -> 3 -> 5 -> 2 -> 4 -> None

        '''

        odd = head # 1st node
        temp = head.next # keep head of the even chain to link
        even = head.next # 2nd node

        while even and even.next:
            odd.next = even.next # link the current odd to the next odd
            even.next = even.next.next # link the current even to the next even
            odd = odd.next # move up odd pointer
            even = even.next # move up even pointer
        odd.next = temp # attach the even chain to the last odd
        return head
