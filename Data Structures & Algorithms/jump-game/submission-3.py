"""
count = 2
bool = False
nums = [1, 2, 1, 0, 1]
              ^
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        count = 1

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < count:
                count += 1
            else:
                count = 1
        return count == 1

        