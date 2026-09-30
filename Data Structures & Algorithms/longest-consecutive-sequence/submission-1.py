class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        total = set(nums)
        curr = set()
        visited = set()

        for i in range(len(nums)):
            curr.clear()
            num = nums[i]
            if num in visited:
                continue
            
            visited.add(num)
            curr.add(num)

            while num + 1 in total:
                curr.add(num+1)
                visited.add(num+1)
                num = num+1
            
            res = max(res, len(curr))
        
        return res