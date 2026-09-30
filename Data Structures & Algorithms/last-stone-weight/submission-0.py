import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = [-stone for stone in stones]
        heapq.heapify(res)

        while len(res) > 1:
            x = -heapq.heappop(res)
            y = -heapq.heappop(res)

            if x < y:
                y -= x
                heapq.heappush(res, -y)
            elif y < x:
                x -= y
                heapq.heappush(res, -x)
        
        if res:
            return -res[0]
        return 0