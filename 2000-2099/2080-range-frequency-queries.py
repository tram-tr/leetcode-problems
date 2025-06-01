# https://leetcode.com/problems/range-frequency-queries/

class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.pos = defaultdict(list)
        for i in range(len(arr)):
            self.pos[arr[i]].append(i)

    def binary_search(self, arr, target):
        l = 0
        r = len(arr)

        while l < r:
            m = l + (r - l) // 2
            if arr[m] > target:
                r = m
            else:
                l = m + 1
        
        return l

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.pos:
            return 0

        l = self.binary_search(self.pos[value], left-1)
        r = self.binary_search(self.pos[value], right)

        return r - l
    


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
