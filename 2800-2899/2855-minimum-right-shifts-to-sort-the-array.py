# https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array/description/

def solution(nums):
    n = len(nums)
    i = 0
    while i + 1 < n and nums[i] < nums[i + 1]:
        i += 1

    if i == n - 1:
        return 0
    
    i += 1
    k = i

    while i + 1 < n and nums[i] < nums[i + 1]:
        i += 1

    if i != n - 1:
        return -1
    
    if nums[k] < nums[0] and nums[n - 1] < nums[0]:
        return n - k
    
    return -1

nums = [3, 4, 5, 1, 2]
print(solution(nums)) # 2

nums = [1, 3, 5]
print(solution(nums)) # 0

nums = [2, 1, 4]
print(solution(nums)) # -1

nums = [1,2,5,4]
print(solution(nums)) # -1
