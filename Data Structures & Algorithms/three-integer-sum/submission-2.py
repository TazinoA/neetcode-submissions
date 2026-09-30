class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0 and len({i, j, k}) == 3:
                        values = sorted([nums[i], nums[j], nums[k]])
                        res.add(tuple(values))
        return list(res)

        