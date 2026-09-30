"""
Brute force O(k % len(arr) * n):
    repeat k % len(arr) times:
        shift all elements down, and replace first with original last

optimal O(n):
    build an index list of where all elements will end up
    each element ends up in (index + k) % len(arr)

"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        cop = nums.copy()
        indices = [(i+k)%len(nums) for i in range(len(nums))]
        
        for i in range(len(nums)):
            nums[indices[i]] = cop[i]
        

        