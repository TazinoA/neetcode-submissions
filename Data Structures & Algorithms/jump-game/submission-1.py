"""
count = 2
bool = False
nums = [1, 2, 1, 0, 1]
              ^
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        count = 1
        res = True

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < count:
                res = False
                count += 1
            else:
                res = True
                count = 1
        return res

        