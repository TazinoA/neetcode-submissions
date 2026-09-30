"""
[2, 3, 0, 1, 4]
        ^
[inf,inf,inf,1,0]

nums[i] = 0
len(nums) - i - 1 = 5 - 2 - 1 = 2
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * len(nums)
        dp[-1] = 0

        for i in range(len(nums)-2, -1, -1):
            if nums[i] >= len(nums) - i - 1:
                dp[i] = 1
            elif nums[i] == 0:
                continue
            else:
                dp[i] = 1 + min(dp[i+1: i+nums[i]+1])
        
        return dp[0]
