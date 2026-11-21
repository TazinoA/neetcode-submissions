import heapq
"""
keep max heap of (key, val), key = abs(x - val) size should be k
loop through whole array and fill heap, return all vals
"""
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        max_heap = []

        for num in arr:
            key = abs(num - x)
            heapq.heappush_max(max_heap, (key, num))

            if len(max_heap) > k:
                heapq.heappop_max(max_heap)
        
        return sorted([i[1] for i in max_heap])