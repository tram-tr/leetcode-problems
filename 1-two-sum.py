class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a dictionary to store the complement of each number encountered
        hashMap = {}
        res = [0, 0]
       
        for i in range(len(nums)):
            # check if the current number is already in the hashMap
            if nums[i] in hashMap:
                # hashMap[current number] = index of its complement
                res[0] = hashMap[nums[i]]
                res[1] = i
                break
            
            # add the current number and its complement into the hashMap
            hashMap[target - nums[i]] = i
     
        return res
