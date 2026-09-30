"""
[1, 5, 10]
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
       ^
min(1+dp[i-coin], dp[i])
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [float('inf')] * (amount+1)
        res[0] = 0

        for i in range(1, len(res)):
            for coin in coins:
                if i - coin >= 0:
                    res[i] = min(res[i],1+ res[i-coin])

        return res[-1] if res[-1] != float('inf') else -1        