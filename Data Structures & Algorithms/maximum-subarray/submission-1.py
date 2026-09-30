"""
curr = 2
res = 2

[2, -3, 4, -2, 2, 1, -1, 4]
 ^
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        res = nums[0]
        curr = 0

        for num in nums:
            if curr + num < 0:
                res = max(res, curr + num)
                curr = 0
            else:
                curr += num
                res = max(res, curr)
        return res

        
        