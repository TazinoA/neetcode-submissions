class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        res = [0]
        res += [float('inf')] * amount
        
        for i in range(1, len(res)):
            for coin in coins:
                if i - coin >= 0:
                    res[i] = min(res[i], 1 + res[i - coin])
        return res[-1] if res[-1] != float('inf') else -1
