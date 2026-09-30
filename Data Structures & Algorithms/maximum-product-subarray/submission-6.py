class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                res = max(res, math.prod(nums[i:j]))
        
        return res

        