class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        val_count = 0
        for num in nums[:]:
            if num == val:
                val_count += 1
                nums.remove(val)
        return n - val_count