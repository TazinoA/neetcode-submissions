"""
binary search
keep track of largest less than target and smallest greater than target
if you find target return n
else retur index +- 1
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        insert_indexes = [[float('-inf'),-1], [float('inf'),-1]]
        while left <= right:
            mid = (left + right) // 2
            print(mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
                if nums[mid] > insert_indexes[0][0]:
                    insert_indexes[0][0] = nums[mid]
                    insert_indexes[0][1] = mid + 1
            else:
                right = mid - 1
                if nums[mid] < insert_indexes[1][0]:
                    insert_indexes[1][0] = nums[mid]
                    insert_indexes[1][1] = mid
        
        #choose the index where the target is closest to values found
        if abs(insert_indexes[0][0] - target) < abs(insert_indexes[1][0] - target):
            return insert_indexes[0][1]
        else:
            return insert_indexes[1][1]