class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        #also track robbed houses
        houses = [[0]]
        if nums[1] > nums[0]:
            houses.append([1])
        else:
            houses.append([0])

        res = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)):
            res.append(max(nums[i] + res[i-2], res[i-1]))

            if nums[i] + res[i - 2] > res[i-1]:
                houses.append([house for house in houses[i-2]] + [i])
            else:
                houses.append(houses[i-1])
        
        print(houses)
        return res[-1]
