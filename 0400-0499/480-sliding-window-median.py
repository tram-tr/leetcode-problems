# https://leetcode.com/problems/sliding-window-median/

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        max_heap = [] 
        min_heap = []
        res = []

        # first window into max_heap
        for i in range(k):
            heapq.heappush(max_heap, (-nums[i], i))
        
        # move the top ceil(k/2) elements into min_heap
        for _ in range(k-k//2):
            num, idx = heapq.heappop(max_heap)
            heapq.heappush(min_heap, (-num, idx))

        # record the first median
        # handle odd and even k
        if k % 2 == 1:
            res.append(float(min_heap[0][0]))
        else:
            res.append((-max_heap[0][0] + min_heap[0][0]) / 2)

        # sliding window
        for i in range(k, len(nums)):
            # insert new num
            if nums[i] >= min_heap[0][0]:
                heapq.heappush(min_heap, (nums[i], i))
                # rebalance if remove from the lower half
                if nums[i-k] <= min_heap[0][0]:
                    num, idx = heapq.heappop(min_heap)
                    heapq.heappush(max_heap, (-num, idx))
            else:
                heapq.heappush(max_heap, (-nums[i], i))
                # rebalance if remove from the upper half
                if nums[i-k] >= min_heap[0][0]:
                    num, idx = heapq.heappop(max_heap)
                    heapq.heappush(min_heap, (-num, idx))

            # prune any elements whose idx <= i-k
            while max_heap and max_heap[0][1] <= i-k:
                heapq.heappop(max_heap)
            while min_heap and min_heap[0][1] <= i-k:
                heapq.heappop(min_heap)
            
            # handle odd and even k
            if k % 2 == 1:
                res.append(float(min_heap[0][0]))
            else:
                res.append((min_heap[0][0] + -max_heap[0][0]) / 2.0)

        return res

                
            

            
