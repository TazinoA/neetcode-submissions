class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        res = float('-inf')
        curr = 0

        for num in nums:
            if curr + num > 0:
                curr += num
                res = max(res, curr)
            else:
                curr = 0
                res = max(res, curr + num)
        return res

        