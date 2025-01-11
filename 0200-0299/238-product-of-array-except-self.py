class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # corner case : 0
        # [0, 0, 0] -> [0, 0, 0]
        # [0, 1, 0] -> [0, 0, 0] 
        # [0, 1, 1] -> [1, 0, 0]

        # brute-force: O(N^2)
        '''
        ans = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                print(j)
                if (i != j):
                    product *= nums[j]
            ans.append(product)
        '''
        # Time: O(N)
        # Space: O(N)
        ans = [1] * len(nums)
        # 1, [2, 3, 4]
        # [1], 2, [3, 4]
        # [1, 2], 3, [4]
        # [1, 2, 3], 4
        # [1, 2, 3, 4] -> [1, 1, 2, 6] -> [24, 12, 8, 6]
        for i in range(len(nums)):
            if i > 0:
                ans[i] = ans[i-1] * nums[i-1]

        right = 1
        for i in reversed(range(len(nums))):
            ans[i] = ans[i] * right
            right *= nums[i]
       
        return ans
