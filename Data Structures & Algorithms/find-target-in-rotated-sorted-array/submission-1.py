class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(arr, high, low, target):
            l, r = low, high
            while l <= r:
                m = (l+r)//2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m -1
                else:
                    l = m + 1
            return -1
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l+r)//2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
    
        res = binarySearch(nums,l-1, 0, target)
        if res != -1:
            return res
        else:
            return binarySearch(nums,len(nums)-1, l, target)
            
        