"""
max = 2 (2, 2, 2)
min = 2  (6, 6, 3)
res = 2
temp = 2

nums = [2, 3, -2, 4]
           ^
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax, currMin, res = 1, 1, nums[0]

        for num in nums:
            temp = currMin
            currMin = min(currMin * num, currMax * num, num)
            currMax = max(temp * num, currMax * num, num)
            res = max(currMin, currMax, res)
        return res
        