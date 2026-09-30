class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def houseRob(arr):
            rob1, rob2 = 0, 0
            for num in arr:
                tmp = rob2
                rob2 = max(num+rob1, rob2)
                rob1 = tmp
            return rob2
        
        return max(houseRob(nums[1:]), houseRob(nums[:-1]))