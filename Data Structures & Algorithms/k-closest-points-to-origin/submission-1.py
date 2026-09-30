import heapq
"""
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        for x,y in points:
            distance = math.sqrt((x*x) + (y*y))
            heapq.heappush(res, [-distance, [x,y]])
            while len(res) > k:
                heapq.heappop(res)
        
        
        return [i[1] for i in res]
