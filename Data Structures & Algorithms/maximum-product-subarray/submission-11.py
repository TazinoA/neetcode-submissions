class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMin, currMax = 1, 1
        for num in nums:
            temp = currMax * num
            currMax = max(num, currMin*num, currMax*num)
            currMin = min(num, temp, currMin*num)
            res = max(res, currMax)
           
            if num == 0:
                currMin, currMax = 1, 1
        return res
