"""
[2, 3, 0, 1, 4]
    ^
[0,1,1,2,2]

nums[i] = 0
len(nums) - i - 1 = 5 - 2 - 1 = 2
O(n*max(nums))
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * len(nums)
        dp[0] = 0

        for i in range(len(nums)):
            j = 0
            while j < nums[i] and i+j+1 < len(nums):
                dp[i+j+1] = min(dp[i+j+1], 1 + dp[i])
                j+=1
        return dp[-1]
