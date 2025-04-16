# https://leetcode.com/problems/reverse-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if not head:
    #         return None
           
    #     # use two pointers prev and curr
    #     # initially prev is None and curr points to head
    #     # let next to be the next node of curr before reversing curr, next = curr.next
    #     # set curr.next = prev
    #     # set prev = curr and curr = next

    #     # head -> [1] -> [2] -> [3] -> None
    #     # curr -> [1] -> [2] -> [3] -> None
    #     # prev -> None

    #     # nxt -> [2] -> [3] -> None
    #     # curr.next -> None => [1] -> None
    #     # prev -> [1] -> None
    #     # curr -> [2] -> [3] -> None

    #     # nxt -> [3] -> None
    #     # curr.next -> [1] -> None => [2] -> [1] -> None
    #     # prev -> [2] -> [1] -> None
    #     # curr -> [3] -> None

    #     # nxt -> None
    #     # curr.next -> [2] => [3] -> [2] -> [1] -> None
    #     # prev -> [3] -> [2] -> [1] -> None
    #     # curr -> None

    #     prev = None
    #     curr = head
    #     nxt = None


    #     while curr:
    #         nxt = curr.next # save the next node
    #         curr.next = prev # reverse the link
    #         prev = curr # move prev forward
    #         curr = nxt # move curr forward


    #     return prev

    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if not head or not head.next:
    #         return head

    #     # do the reverse operation for head.next
    #     # set head.next.next = head
    #     # set head.next = None
    #     new_head = self.reverseList(head.next)
    #     head.next.next = head # head.next is end of the newly reversed list
    #     head.next = None

    #     return new_head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # dummny.next -> None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = dummy.next
            dummy.next = curr
            curr = nxt

        return dummy.next

        
