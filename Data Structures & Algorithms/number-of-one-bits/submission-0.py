class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for bit in bin(n):
            if bit == "1":
                count += 1
        return count
        