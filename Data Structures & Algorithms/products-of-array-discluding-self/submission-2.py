"""
nums = [1,2,3,0,4,0,9,8]
res  = [0,0,0,0,0,0,0,0]
keep a count of all indexes with 0, if more than 1, whole array is 0
if only 1 zero keep total without zero, else just divide
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        total = math.prod(nums)
        total_without_zero = 1

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                total_without_zero *= num
        
        if zero_count > 1:
            return [0] * len(nums)
        else:
            return [total//num if num != 0 else total_without_zero for num in nums]
