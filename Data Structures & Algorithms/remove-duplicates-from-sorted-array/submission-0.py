class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        for num in nums[:]:
            if num in seen:
                nums.remove(num)
            else:
                seen.add(num)
        
        return len(seen)
