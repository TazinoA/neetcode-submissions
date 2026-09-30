class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        total = set(nums)
        visited = set()

        for num in nums:
            length = 0
            if num in visited:
                continue
            
            visited.add(num)
            length += 1

            while num + 1 in total:
                length += 1
                visited.add(num+1)
                num = num+1
            
            res = max(res, length)
        
        return res