import heapq
"""
klogn
klogn
"""
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = [-num for num in nums]
        self.k = k
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, -val)
        curr = []

        for _ in range(self.k):
            if not self.nums:
                break
            curr.append(heapq.heappop(self.nums))
        res = -curr[-1]
        for num in curr:
            heapq.heappush(self.nums, num)
        return res
        
