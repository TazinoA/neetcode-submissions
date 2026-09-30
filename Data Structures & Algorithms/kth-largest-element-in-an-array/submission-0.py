"""
heappush and only keep k elements

n log k
"""
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []

        for num in nums:
            heapq.heappush(res, num)
            while len(res) > k:
                heapq.heappop(res)
        
        return res[0]