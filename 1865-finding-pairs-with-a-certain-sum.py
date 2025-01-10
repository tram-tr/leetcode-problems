# https://leetcode.com/problems/finding-pairs-with-a-certain-sum/

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.counter = Counter(self.nums2)

    def add(self, index: int, val: int) -> None:
        prev = self.nums2[index]
        self.nums2[index] += val
        self.counter[prev] -= 1
        self.counter[self.nums2[index]] += 1
        

    def count(self, tot: int) -> int:
        tot_count = 0
        for num in self.nums1:
            tot_count += self.counter[tot - num]

        return tot_count
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
