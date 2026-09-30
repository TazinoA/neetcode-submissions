class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = prices[0]
        res = 0

        for price in prices:
            curr_min = min(curr_min, price)
            profit = price - curr_min
            res = max(res, profit)
        return res
        