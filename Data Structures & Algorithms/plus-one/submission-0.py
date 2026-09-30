class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for digit in digits:
            num += str(digit)
        res = str(int(num) + 1)

        return [int(i) for i in res]
