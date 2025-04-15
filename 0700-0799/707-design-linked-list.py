# https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val: int, next = None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None # head pointer to track the start of the linked list

    # get the value of index node in the linked list
    # traversing the list
    # time: O(N)
    def get(self, index: int) -> int:
        curr = self.head
        while curr is not None and index > 0:
            curr = curr.next
            index -= 1
        
        if curr is None:
            return -1

        return curr.val
        
    # directly updating the head pointer
    # time: O(1)
    def addAtHead(self, val: int) -> None:
        node = Node(val)
        if not self.head:
            self.head = node
            return
        
        node.next = self.head
        self.head = node
        
    # traverse to the tail and append
    # O(N)
    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if self.head is None:
            self.head = node
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = node

    # traverse to index - 1 and insert
    # time: O(N)
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        node = Node(val)
        curr = self.head
        while curr is not None and index > 1:
            curr = curr.next
            index -= 1
        
        if curr is None:
            return
        
        node.next = curr.next
        curr.next = node
        
    # traverse to index and delete
    # time: O(N)
    def deleteAtIndex(self, index: int) -> None:
        if self.head is None: 
            return

        if index == 0:
            self.head = self.head.next
            return

        curr = self.head
        prev = None
        while curr is not None and index > 0:
            prev = curr
            curr = curr.next
            index -= 1
        
        if curr is None:
            return
        
        prev.next = curr.next
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
