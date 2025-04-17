# https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    # maintain the order of the data because if we have more data than capacity, we have to remove LRU data 
    # using queue would be hard to keep track the Most Recently Used order if the problem is asking for O(1)
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = defaultdict(int)
        self.dummy_lru = Node(0, 0) # least recently used
        self.dummy_mru = Node(0, 0) # most recently used
        # link nodes
        '''
        dummy lru (None) <-> lru <-> ... <-> mru <-> dummy_mru (None)
        '''
        self.dummy_lru.next = self.dummy_mru
        self.dummy_mru.prev = self.dummy_lru        

    # return the value of the key if the key exists
    def get(self, key: int) -> int:
        if key in self.cache: # if key exists
            # evict the key
            self.remove(self.cache[key]) # remove key at current position
            self.insert(self.cache[key]) # add key to the tail of the linked list
            return self.cache[key].val
        return -1
        
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache: # if key exists
            self.remove(self.cache[key]) # remove key at the current position to evict
        # insert the key-value pair to the cache and linked list
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # check the capacity
        if len(self.cache) > self.capacity:
            # remove the least recently used key
            lru = self.dummy_lru.next 
            self.remove(lru)
            del self.cache[lru.key]

    def insert(self, node: Node) -> None: # to insert update the most recently used key
        '''
        before: ... <-> prev_mru <-> None
        after: ... <-> prev_mru <-> node <-> None

        '''
        prev_mru = self.dummy_mru.prev
        dummy = self.dummy_mru # dummy tail
        prev_mru.next = node
        dummy.prev = node
        node.next = dummy
        node.prev = prev_mru
        
    def remove(self, node: Node) -> None:
        '''
        before: ... <-> prev node <-> node <-> next node <-> ...
        after: ... <-> prev node <-> next node <-> ...
        '''
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
