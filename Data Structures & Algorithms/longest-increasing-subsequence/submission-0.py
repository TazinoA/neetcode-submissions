"""
[9, 1, 4, 2, 3, 3,2, 7]
 j                 i

[1, 1, 2, 2, 3, 3, 2, 4]
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 1
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            j = 0
            while j < i:
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    res = max(res, dp[i])
                j += 1
        return res
        