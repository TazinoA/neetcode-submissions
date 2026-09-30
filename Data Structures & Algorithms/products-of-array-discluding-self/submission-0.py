class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        curr = 1

        for i in range(len(nums)):
            curr = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                curr *= nums[j]
            res.append(curr)
        return res

        