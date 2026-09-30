class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        res = []
        max_val = 0
        max_key = 0

        for i in range(k):
            max_val = 0
            for key, value in freq.items():
                if value > max_val and key not in res:
                    max_val = value
                    max_key = key
            res.append(max_key)
            
        return res
        