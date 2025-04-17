# https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:

    def __init__(self):
        self.nums = [] # 0-indexed list of nums
        self.map = defaultdict(int)

    # O(1)
    def insert(self, val: int) -> bool:
        if val in self.map:
            return False

        self.nums.append(val)
        self.map[val] = len(self.nums) - 1
        return True
        
    # O(1)
    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        idx = self.map[val]
        self.map[self.nums[-1]] = idx
        self.nums[-1], self.nums[idx] = self.nums[idx], self.nums[-1]
        self.nums.pop() # O(1)
        del self.map[val]

        return True
        
    # O(1)
    def getRandom(self) -> int:
        idx = random.randrange(len(self.nums))
        return self.nums[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
