class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = prices[0]
        curr_max = 0

        for i in range(len(prices)):
            if prices[i] < curr_min:
                curr_min = prices[i]
            profit = prices[i] - curr_min
            if profit > curr_max:
                curr_max = profit
        return curr_max