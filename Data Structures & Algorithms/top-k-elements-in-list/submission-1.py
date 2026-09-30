"""
hashmap with count and val
go through map and add to heap and keep heap length = k
"""
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        maxHeap = []
        for num, freq in hashMap.items():
            if len(maxHeap) == k:
                heapq.heappush(maxHeap, [freq, num])
                heapq.heappop(maxHeap)
            else:
                heapq.heappush(maxHeap, [freq, num])
        print(maxHeap)
        return [i[1] for i in maxHeap]