class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n + 1):
            res.append(self.hammingWeight(i))
        return res

    


    def hammingWeight(self, n: int) -> int:
        count = 0
        for bit in bin(n):
            if bit == "1":
                count += 1
        return count
        